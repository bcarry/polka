import numpy as np
import matplotlib.pyplot as plt

import polka
import rocks


def get_colors(N, cmap="turbo"):
    """
    Get a list of unique colors.

    Parameters
    ----------
    N : int
        The number of unique colors to return.
    cmap : str
        The matplotlib colormap to sample. Default is 'turbo'

    Returns
    -------
    list of str
        A list of color-hexcodes.

    """
    COLORS = plt.get_cmap(cmap, N)
    return [mpl.colors.rgb2hex(COLORS(i)[:3]) for i in range(N)]


def plot_pc(pc, models, label_sources=False, save=None):
    """Plot polrimetric phase curve and model fits."""

    fig, ax = plt.subplots()

    # 

    # Observations
    if label_sources and pc.src is not None:

        for s in np.unique(pc.src):
            cond = np.where(pc.src == s)
            ax.errorbar(
                pc.phase[cond],
                pc.pol[cond],
                yerr=pc.pol_err[cond],
                ls="",
                marker="o",
                label=s,
            )
    else:
        ax.errorbar(
            pc.phase,
            pc.pol,
            yerr=pc.pol_err,
            ls="",
            marker="o",
            label=f"Observations",
        )

    # Models
    for i, model in enumerate(models):
        model = getattr(pc, model)  # switch to actual model instance

        phase_eval = np.linspace(0, pc.phase.max(), 100)
        params = model.PARAMS
        pol_eval = model.eval(phase_eval)

        label = ": ".join(
            [
                model.NAME,
                ", ".join(
                    [
                        f"{p}: {v:.2f}"
                        for p, v in zip(params, [getattr(model, p) for p in params])
                    ]
                ),
            ]
        )

        ax.plot(phase_eval, pol_eval, label=label, ls="-")

    # Axes
    ax.set(
        xlabel="Phase Angle / deg",
        ylabel="Linear polarisation",
        xlim=(0, pc.phase.max()),
    )

    # Legend
    ax.legend(
        title=(
            f"({pc.target.number}) {pc.target.name}"
            if isinstance(pc.target, rocks.Rock)
            else None
        )
    )

    # Export
    if save is None:
        plt.show()
    else:
        fig.tight_layout()
        fig.savefig(save)
        print(f"Saved figure under {save}")
