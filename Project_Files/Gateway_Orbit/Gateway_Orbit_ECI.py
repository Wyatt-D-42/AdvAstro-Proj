import spiceypy as spice
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Load kernels via your meta-kernel
#    (same gateway_meta.txt you already have)
# -------------------------------------------------
spice.furnsh("gateway_meta.txt")

# -------------------------------------------------
# 2. Time window inside the SPK coverage
# -------------------------------------------------
utc_start = "2020-01-05 T00:00:00"
utc_end   = "2020-03-05 T00:00:00"

et_start = spice.str2et(utc_start)
et_end   = spice.str2et(utc_end)

N = 2000
times = np.linspace(et_start, et_end, N)

# -------------------------------------------------
# 3. NAIF IDs
# -------------------------------------------------
DSG_ID   = "-60000"   # DSG spacecraft from nrho.lbl
EARTH_ID = "EARTH"    # 399
MOON_ID  = "MOON"     # 301

# -------------------------------------------------
# 4. States in Earth-centered inertial frame (J2000)
# -------------------------------------------------
# DSG w.r.t. EARTH in J2000 (this is basically ECI)
dsg_states_eci, _ = spice.spkezr(
    targ   = DSG_ID,
    et     = times,
    ref    = "J2000",
    abcorr = "NONE",
    obs    = EARTH_ID,
)
r_dsg_eci = dsg_states_eci[:, :3]   # (N,3)

# Moon w.r.t. EARTH in J2000
moon_states_eci, _ = spice.spkezr(
    targ   = MOON_ID,
    et     = times,
    ref    = "J2000",
    abcorr = "NONE",
    obs    = EARTH_ID,
)
r_moon_eci = moon_states_eci[:, :3]

# -------------------------------------------------
# 5. 3D plot: Earth at origin, Moon orbiting, DSG precessing
# -------------------------------------------------
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

# Optional: subsample so the plot isn't too dense
step = slice(0, N, 3)

# DSG trajectory
ax.plot(
    r_dsg_eci[step, 0], r_dsg_eci[step, 1], r_dsg_eci[step, 2],
    label="DSG NRHO",
)

# Moon trajectory
ax.plot(
    r_moon_eci[step, 0], r_moon_eci[step, 1], r_moon_eci[step, 2],
    linestyle="--",
    label="Moon orbit",
)

# Earth at origin
ax.scatter(0.0, 0.0, 0.0, s=80, color="blue", label="Earth")

ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.set_title("DSG NRHO and Moon in Earth-Centered Inertial Frame (J2000)")

# --- make the 3D aspect ratio equal-ish ---
x = r_dsg_eci[:, 0]
y = r_dsg_eci[:, 1]
z = r_dsg_eci[:, 2]

max_range = max(x.max() - x.min(), y.max() - y.min(), z.max() - z.min()) / 2.0
mid_x = (x.max() + x.min()) / 2.0
mid_y = (y.max() + y.min()) / 2.0
mid_z = (z.max() + z.min()) / 2.0

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

ax.legend()
plt.tight_layout()
plt.show()

spice.kclear()

