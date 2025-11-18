import spiceypy as spice
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Load kernels
# -------------------------------------------------
spice.furnsh('gateway_meta.txt')

# -------------------------------------------------
# 2. Time window (inside DSG SPK coverage)
# -------------------------------------------------
utc_start = '2020-01-05 T00:00:00'
utc_end   = '2021-01-05 T00:00:00'

et_start = spice.str2et(utc_start)
et_end   = spice.str2et(utc_end)
N = 2000
times = np.linspace(et_start, et_end, N)

# -------------------------------------------------
# 3. NAIF IDs
# -------------------------------------------------
DSG_ID   = '-60000'
EARTH_ID = 'EARTH'
MOON_ID  = 'MOON'
SUN_ID   = 'SUN'

# -------------------------------------------------
# 4. States in Sun-centered J2000
# -------------------------------------------------
# DSG, Earth, Moon w.r.t. SUN
dsg_sun,   _ = spice.spkezr(DSG_ID,   times, 'J2000', 'NONE', SUN_ID)
earth_sun, _ = spice.spkezr(EARTH_ID, times, 'J2000', 'NONE', SUN_ID)
moon_sun,  _ = spice.spkezr(MOON_ID,  times, 'J2000', 'NONE', SUN_ID)

r_dsg_sun   = dsg_sun[:, :3]
r_earth_sun = earth_sun[:, :3]
r_moon_sun  = moon_sun[:, :3]

# -------------------------------------------------
# 5. Zoomed coordinates riding with Earth
#    (still computed from Sun-centered states)
# -------------------------------------------------
r_dsg_zoom  = r_dsg_sun   - r_earth_sun
r_moon_zoom = r_moon_sun  - r_earth_sun

# -------------------------------------------------
# 6. Plot: left = Sun-centered, right = zoom around Earth
# -------------------------------------------------
fig = plt.figure(figsize=(12, 5))

# ---------- LEFT: Sun-centered big picture ----------
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

ax1.plot(r_earth_sun[:, 0], r_earth_sun[:, 1], r_earth_sun[:, 2],
         'b--', label='Earth orbit')
ax1.plot(r_moon_sun[:, 0], r_moon_sun[:, 1], r_moon_sun[:, 2],
         color='orange', alpha=0.6, label='Moon trajectory')
ax1.plot(r_dsg_sun[:, 0], r_dsg_sun[:, 1], r_dsg_sun[:, 2],
         color='green', label='DSG NRHO')

ax1.scatter(0, 0, 0, color='gold', s=80, label='Sun')

ax1.set_xlabel('X (km)')
ax1.set_ylabel('Y (km)')
ax1.set_zlabel('Z (km)')
ax1.set_title('Sun-centered (J2000)')
ax1.legend()

# Make the view roughly top-down on the ecliptic
ax1.view_init(elev=45, azim=45)

# ---------- RIGHT: zoom around Earth ----------
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

ax2.plot(r_dsg_zoom[:, 0],  r_dsg_zoom[:, 1],  r_dsg_zoom[:, 2],
         label='DSG NRHO')
ax2.plot(r_moon_zoom[:, 0], r_moon_zoom[:, 1], r_moon_zoom[:, 2],
         'orange', alpha=0.7, label='Moon orbit')

# Earth at origin in the zoomed frame
ax2.scatter(0, 0, 0, color='b', s=50, label='Earth')

ax2.set_xlabel('X (km)')
ax2.set_ylabel('Y (km)')
ax2.set_zlabel('Z (km)')
ax2.set_title('Zoomed view near Earth')
ax2.legend()

# Make axes limits nice and tight around the NRHO
max_extent = np.max(np.linalg.norm(r_dsg_zoom, axis=1))
R = 1.2 * max_extent
for a in (ax2.set_xlim, ax2.set_ylim, ax2.set_zlim):
    a(-R, R)

ax2.view_init(elev=30, azim=45)

plt.tight_layout()
plt.show()

spice.kclear()
