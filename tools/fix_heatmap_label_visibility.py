from pathlib import Path

p = Path("tools/rebuild_heatmaps_80pct.py")
s = p.read_text()

old_block = """    ax.set_title(title, fontsize=18, fontweight="bold", pad=18)
    ax.set_xlabel("")
    ax.set_ylabel("")

    ax.set_xticks(np.arange(cols) + 0.5)
    ax.set_yticks(np.arange(rows) + 0.5)
    ax.set_xticklabels(pivot.columns, rotation=45, ha="right", fontsize=12)
    ax.set_yticklabels(pivot.index, rotation=0, fontsize=12)

    ax.tick_params(axis="both", which="major", labelsize=12)

    # Keep colorbar labels readable as well.
    try:
        cbar = mappable.colorbar
        cbar.ax.tick_params(labelsize=11)
    except Exception:
        pass

    add_80pct_annotations(ax, fig, pivot, mappable)

    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=240, bbox_inches="tight")
    plt.close(fig)
"""

new_block = """    # Make title and labels clearly visible like the other line/bar charts.
    ax.set_title(title, fontsize=24, fontweight="bold", pad=24)
    ax.set_xlabel("")
    ax.set_ylabel("")

    ax.set_xticks(np.arange(cols) + 0.5)
    ax.set_yticks(np.arange(rows) + 0.5)

    ax.set_xticklabels(
        pivot.columns,
        rotation=45,
        ha="right",
        rotation_mode="anchor",
        fontsize=15,
        fontweight="medium",
    )
    ax.set_yticklabels(
        pivot.index,
        rotation=0,
        fontsize=15,
        fontweight="medium",
    )

    ax.tick_params(axis="both", which="major", labelsize=15, pad=6)

    # Make colorbar labels readable too.
    try:
        cbar = mappable.colorbar
        cbar.ax.tick_params(labelsize=14)
    except Exception:
        pass

    add_80pct_annotations(ax, fig, pivot, mappable)

    # Give more room so title and tick labels stay visible.
    fig.subplots_adjust(top=0.86, bottom=0.30, left=0.18, right=0.97)

    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=260, bbox_inches="tight", facecolor="white")
    plt.close(fig)
"""

if old_block not in s:
    raise SystemExit("Target block not found in tools/rebuild_heatmaps_80pct.py")

s = s.replace(old_block, new_block)
p.write_text(s)

print("Patched tools/rebuild_heatmaps_80pct.py successfully.")
