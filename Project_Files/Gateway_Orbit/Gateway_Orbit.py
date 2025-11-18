import spiceypy as spice
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Load kernels via your meta-kernel
# -------------------------------------------------
spice.furnsh('gateway_meta.txt')

# -------------------------------------------------
# 2. Time window inside the SPK coverage
# -------------------------------------------------
utc_start = '2020-01-05 T00:00:00'
utc_end   = '2020-03-05 T00:00:00'

et_start = spice.str2et(utc_start)
et_end   = spice.str2et(utc_end)

N = 2000
times = np.linspace(et_start, et_end, N)

# -------------------------------------------------
# 3. NAIF IDs
# -------------------------------------------------
DSG_ID   = '-60000'   # DSG spacecraft
EARTH_ID = 'EARTH'    # 399
MOON_ID  = 'MOON'     # 301

# -------------------------------------------------
# 4. States in J2000, Moon-centered
# -------------------------------------------------
# DSG w.r.t. MOON in J2000
dsg_states_moon, _ = spice.spkezr(
    targ   = DSG_ID,
    et     = times,
    ref    = 'J2000',
    abcorr = 'NONE',
    obs    = MOON_ID
)
r_dsg_moon = dsg_states_moon[:, :3]

# Earth w.r.t. MOON in J2000
earth_states_moon, _ = spice.spkezr(
    targ   = EARTH_ID,
    et     = times,
    ref    = 'J2000',
    abcorr = 'NONE',
    obs    = MOON_ID
)
r_e_moon = earth_states_moon[:, :3]
v_e_moon = earth_states_moon[:, 3:]

# -------------------------------------------------
# 5. Build Moon-centered EM rotating frame
# -------------------------------------------------
# x-axis: Moon → Earth
x_hat = r_e_moon / np.linalg.norm(r_e_moon, axis=1, keepdims=True)

# z-axis: orbital angular momentum of Earth about Moon
h_vec = np.cross(r_e_moon, v_e_moon)
z_hat = h_vec / np.linalg.norm(h_vec, axis=1, keepdims=True)

# y-axis: completes right-handed triad
y_hat = np.cross(z_hat, x_hat)
y_hat = y_hat / np.linalg.norm(y_hat, axis=1, keepdims=True)

# -------------------------------------------------
# 6. Rotate DSG and Earth positions into this frame
# -------------------------------------------------
r_dsg_rot = np.zeros_like(r_dsg_moon)
r_e_rot   = np.zeros_like(r_e_moon)

for k in range(N):
    C_rot_J2000 = np.column_stack((x_hat[k], y_hat[k], z_hat[k]))  # columns are unit axes
    r_dsg_rot[k] = C_rot_J2000.T @ r_dsg_moon[k]
    r_e_rot[k]   = C_rot_J2000.T @ r_e_moon[k]

# -------------------------------------------------
# 7. Plot as seen from Earth: use Y–Z plane
#    (Moon at origin, looking along -X toward the Moon)
# -------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 6))

# Plot NRHO in Y–Z plane
ax.plot(r_dsg_rot[:, 1], r_dsg_rot[:, 2],
        label='DSG NRHO')

# Moon at center
ax.scatter(0, 0, s=60, color='gray', label='Moon')

# Nice symmetric limits around Moon
y = r_dsg_rot[:, 1]
z = r_dsg_rot[:, 2]
R = 1.1 * max(abs(y).max(), abs(z).max())
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)

ax.set_xlabel('Y (km)')
ax.set_ylabel('Z (km)')
ax.set_title('DSG NRHO in Earth–Moon Rotating Frame\nMoon-centered, view from Earth')

ax.set_aspect('equal', 'box')
ax.grid(True)
ax.legend(loc='upper right')
fig.tight_layout()
plt.show()

spice.kclear()

