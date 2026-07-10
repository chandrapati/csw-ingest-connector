#!/usr/bin/env python3
"""Render the CSW Secure Workload *Ingest* virtual appliance architecture diagram.

Same visual language as the other connector guides (F5, NetScaler, vCenter,
AnyConnect, Edge): Cisco navy/blue palette, rounded panels, labelled arrows.
Flow: telemetry sources -> transport (NetFlow/IPFIX/ERSPAN) -> Ingest appliance
(slot-based connectors) -> Secure Workload cluster (flows for visibility/ADM/policy).

Run:  python3 make_architecture.py
Requires: matplotlib
"""
from matplotlib import pyplot as plt
from matplotlib.patches import (FancyBboxPatch, FancyArrowPatch, Circle,
                                 Polygon, Rectangle, Ellipse)

# ---- palette ----------------------------------------------------------------
NAVY = "#00205B"
BLUE = "#007BC7"
CYAN = "#00BCEB"
PURPLE = "#5B3E9E"      # flow/telemetry accent
PURPLE_D = "#3F2A73"
INK = "#1A1A2E"
GREY = "#555555"
PURPLEBG = "#EFEAF7"
BLUEBG = "#EAF4FB"
NAVYBG = "#F3F7FC"
RED = "#B52C2C"

fig, ax = plt.subplots(figsize=(13.0, 8.0), dpi=100)
ax.set_xlim(0, 130)
ax.set_ylim(0, 80)
ax.axis("off")


def panel(x, y, w, h, edge, fc="white", lw=2.2, rounding=1.4, z=1):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rounding}",
        linewidth=lw, edgecolor=edge, facecolor=fc, zorder=z))


def box(x, y, w, h, edge, fc="white", lw=1.4, rounding=0.9, z=2, dashed=False):
    ls = (0, (4, 3)) if dashed else "solid"
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rounding}",
        linewidth=lw, edgecolor=edge, facecolor=fc, linestyle=ls, zorder=z))


def text(x, y, s, size=11, color=INK, weight="normal", ha="center", va="center", z=5):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, zorder=z,
            fontfamily=["Helvetica Neue", "Arial", "DejaVu Sans"])


# ---- Title + Cisco wordmark -------------------------------------------------
text(61, 76.5, "Cisco Secure Workload  \u2013  Ingest Virtual Appliance (Flow / Packet Telemetry)",
     size=17, color=NAVY, weight="bold")

lx = 114.0
heights = [1.6, 2.6, 3.6, 2.6, 1.6, 2.6, 3.6, 4.6, 3.6, 2.6, 1.6]
for i, hh in enumerate(heights):
    ax.add_patch(Rectangle((lx + i * 0.7, 74.4 - hh / 2), 0.30, hh,
                 facecolor=NAVY, edgecolor="none", zorder=5))
text(lx + len(heights) * 0.35, 70.6, "CISCO", size=9.5, color=NAVY, weight="bold")

# =============================================================================
# LEFT PANEL  --  telemetry sources
# =============================================================================
panel(3, 19, 34, 47, PURPLE)
text(20, 62.6, "Telemetry sources", size=13, color=PURPLE_D, weight="bold")
srcs = [
    ("Switches / Routers", "NetFlow v9"),
    ("F5 BIG-IP  \u00b7  Citrix NetScaler", "IPFIX / AppFlow"),
    ("Secure Firewall ASA / FTD", "NSEL"),
    ("Meraki MX", "NetFlow"),
    ("AnyConnect endpoints", "IPFIX / nvzFlow"),
    ("SPAN / TAP mirror", "ERSPAN (GRE)"),
]
for i, (name, proto) in enumerate(srcs):
    yy = 57.5 - i * 6.3
    box(6, yy - 2.4, 28, 5.0, PURPLE, PURPLEBG, lw=1.2, rounding=0.7)
    text(20, yy + 0.4, name, size=8.6, color=INK)
    text(20, yy - 1.5, proto, size=7.8, color=PURPLE_D, weight="bold")

# =============================================================================
# MIDDLE  --  transport / ports
# =============================================================================
text(52, 60.5, "Collector ports", size=10.5, color=NAVY, weight="bold")
box(41, 50.5, 22, 7.4, BLUE, BLUEBG, lw=1.2, rounding=0.7)
text(52, 55.6, "NetFlow v9 / NSEL", size=8.4, color=INK)
text(52, 53.2, "UDP 4729", size=9.2, color=NAVY, weight="bold")
box(41, 41.5, 22, 7.4, BLUE, BLUEBG, lw=1.2, rounding=0.7)
text(52, 46.6, "IPFIX / AppFlow", size=8.4, color=INK)
text(52, 44.2, "UDP 4739", size=9.2, color=NAVY, weight="bold")
box(41, 32.5, 22, 7.4, BLUE, BLUEBG, lw=1.2, rounding=0.7)
text(52, 37.6, "ERSPAN", size=8.4, color=INK)
text(52, 35.2, "GRE  \u00b7  IP proto 47", size=9.0, color=NAVY, weight="bold")

ax.add_patch(FancyArrowPatch((37, 42.5), (40.6, 47), arrowstyle="-|>",
             mutation_scale=16, linewidth=2.2, color=PURPLE, zorder=3))
ax.add_patch(FancyArrowPatch((37, 42.5), (40.6, 36), arrowstyle="-|>",
             mutation_scale=16, linewidth=2.2, color=PURPLE, zorder=3))
ax.add_patch(FancyArrowPatch((63, 45), (72.5, 47), arrowstyle="-|>",
             mutation_scale=22, linewidth=3.2, color=PURPLE, zorder=3))

# =============================================================================
# RIGHT PANEL  --  Ingest appliance + cluster
# =============================================================================
panel(73, 19, 52, 47, BLUE)
text(99, 62.6, "Cisco Secure Workload", size=13, color=BLUE, weight="bold")

# Ingest appliance box with 3 slots
box(76, 44.5, 46, 15.5, NAVY, NAVYBG, lw=1.7, rounding=1.0)
text(99, 57.9, "Ingest Appliance", size=10, color=NAVY, weight="bold")
text(99, 55.6, "8 vCPU \u00b7 8 GB \u00b7 250 GB \u00b7 3 NICs \u00b7 \u2264100 per root scope", size=7.4, color=GREY)
for i in range(3):
    sx = 78.5 + i * 14.6
    box(sx, 45.6, 13, 7.0, BLUE, BLUEBG, lw=1.2, rounding=0.6)
    ax.add_patch(Circle((sx + 2.4, 49.1), 1.15, facecolor=BLUE, edgecolor="white", lw=0.7, zorder=4))
    ax.add_patch(Circle((sx + 2.4, 49.1), 0.42, facecolor="white", zorder=5))
    text(sx + 8.0, 50.0, f"slot {i+1}", size=7.6, color=NAVY, weight="bold")
    text(sx + 8.0, 47.9, "connector", size=6.9, color=GREY)
text(99, 42.6, "\u2264 3 connectors per appliance  \u00b7  ERSPAN auto-provisions 3", size=7.3, color=GREY)

# arrow appliance -> flows store
ax.add_patch(FancyArrowPatch((99, 44.5), (99, 40.5), arrowstyle="-|>",
             mutation_scale=16, linewidth=2, color=NAVY, zorder=3))

# flows cylinder
cx, cy, cw, ch = 82, 30.5, 14, 8
ax.add_patch(Rectangle((cx, cy), cw, ch, facecolor="white", edgecolor=NAVY, lw=1.8, zorder=3))
ax.add_patch(Ellipse((cx + cw / 2, cy + ch), cw, 2.2, facecolor="white", edgecolor=NAVY, lw=1.8, zorder=4))
ax.add_patch(Ellipse((cx + cw / 2, cy), cw, 2.2, facecolor="white", edgecolor=NAVY, lw=1.8, zorder=3))
text(cx + cw / 2, cy + ch / 2 + 0.6, "Flow", size=8.6, color=NAVY, weight="bold")
text(cx + cw / 2, cy + ch / 2 - 1.5, "observations", size=8.0, color=NAVY)

ax.add_patch(FancyArrowPatch((96.5, 34.5), (101, 32), arrowstyle="-|>",
             mutation_scale=14, linewidth=1.8, color=NAVY, zorder=3))
box(101, 29.6, 21, 6.4, BLUE, BLUE, lw=1.0)
text(111.5, 33.6, "Visibility / ADM", size=8.6, color="white", weight="bold")
text(111.5, 31.2, "dependency mapping", size=7.6, color="white")

box(73, 20.4, 52, 3.4, "#E3B7B7", "#FBF0F0", lw=1.2, rounding=0.7)
text(99, 22.1,
     "Ingest = flow visibility. Enforcement stays with the CSW agent / F5 / NetScaler / FMC / cloud.",
     size=8.0, color=RED)

# ---- bottom gradient bar + caption -----------------------------------------
grad_y = 12.5
for i in range(200):
    frac = i / 199
    if frac < 0.6:
        r = 0x00; g = int(0x20 + (frac / 0.6) * (0x7b - 0x20)); b = int(0x5b + (frac / 0.6) * (0xc7 - 0x5b))
    else:
        t = (frac - 0.6) / 0.4
        r = 0x00; g = int(0x7b + t * (0xbc - 0x7b)); b = int(0xc7 + t * (0xeb - 0xc7))
    ax.add_patch(Rectangle((3 + frac * 122, grad_y), 122 / 200 + 0.2, 1.1,
                 facecolor=f"#{r:02x}{g:02x}{b:02x}", edgecolor="none", zorder=2))

text(64, 9.2,
     "Ingest appliance  \u2014  NetFlow v9 / NSEL (4729) \u00b7 IPFIX / AppFlow (4739) \u00b7 ERSPAN (GRE)  \u2192  Secure Workload flow visibility & ADM",
     size=9.6, color=NAVY, weight="bold")

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
out = "csw-ingest-architecture.png"
plt.savefig(out, dpi=100, facecolor="white", bbox_inches="tight", pad_inches=0.15)
print("wrote", out)
