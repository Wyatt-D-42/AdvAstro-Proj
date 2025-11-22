# Tutorial: JWST Orbit & DSN Visibility Analysis with SpiceyPy

## Overview

This tutorial demonstrates how to use **SpiceyPy** (a Python wrapper for the NASA NAIF SPICE toolkit) to perform mission-design tasks. Specifically, we will calculate the orbit of the James Webb Space Telescope (JWST) and determine when it is visible to the Deep Space Network (DSN) stations in Goldstone, Madrid, and Canberra.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/bmdLQN_MYSI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Key Concepts Covered:**

  * Loading SPICE Kernels (Meta-kernels).
  * Time conversion (UTC to Ephemeris Time).
  * Coordinate Frame Transformations (Inertial J2000 $\to$ Topocentric).
  * Geometric Event Finding (Target visibility).

## 1\. Prerequisites

Ensure you have Python 3.7+ installed. Install the required dependencies:

```bash
pip install spiceypy numpy matplotlib
```

## 2\. Project Structure & Setup

SPICE requires data files called "Kernels" to function. Without these files, the code **will not work**.

### Step A: Download the Kernels

Manually download the following kernels from the [NAIF generic server](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/) and the [JWST server](https://naif.jpl.nasa.gov/pub/naif/JWST/kernels/spk/) into a local directory. Each entry includes a direct download link where available:

- [`naif0012.tls`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/naif0012.tls) — Leap seconds.
- [`pck00010.tpc`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00010.tpc) — Planetary constants.
- [`de440.bsp`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de440.bsp) — Planetary ephemeris (DE440).
- [`earth_720101_current.bpc`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/) — Earth orientation/rotation (see PCK directory for latest files).
- [`earthstns_itrf93_201023.bsp`](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/stations/) — DSN station locations (station SPK files directory).
- [`jwst_pred.bsp`](https://naif.jpl.nasa.gov/pub/naif/JWST/kernels/spk/jwst_pred.bsp) — JWST predicted ephemeris (pred).
- [`jwst_rec.bsp`](https://naif.jpl.nasa.gov/pub/naif/JWST/kernels/spk/) — JWST recorded/rec ephemeris (see JWST SPK directory for specific files).
- [`DSN_topo.tf`](https://naif.jpl.nasa.gov/pub/naif/FIDO/kernels/fk/DSN_topo.tf) — DSN station frames (frame kernels).

### Step B: The Meta-Kernel (`jwst_meta.txt`)

Ensure the file `jwst_meta.txt` exists in this directory. This file acts as a manifest, telling SpiceyPy where to look for the files above.

## 3\. Running the Analysis

Run the main script:

```bash
python jwst_visibility.py
```

## 4\. Understanding the Output

The script generates three specific visualizations:

### A. 3D Halo Orbit (Interactive Window)

  * **What it shows:** The trajectory of JWST relative to the Sun-Earth Barycenter (L2 Lagrange point region).
  * **Colors:** The orbit path is colored based on which DSN station currently has a line-of-sight to the spacecraft.
  * **Frame:** J2000 (Inertial).

### B. Visibility Timeline (Interactive Window)

  * **What it shows:** A Gantt-style chart showing communication windows.
  * **Logic:** A station is considered "connected" if JWST is above 0° elevation (the horizon) relative to that station.

### C. Sky Tracks (`jwst_sky_tracks.png`)

  * **What it shows:** The path JWST traces across the local sky for each station.
  * **Frame:** Topocentric (Azimuth/Elevation).
  * **Note:** This file is saved automatically.

## 5\. Technical Explanation: Coordinate Frames

This code relies heavily on transforming vectors between two types of reference frames.

### 1\. The Inertial Frame (J2000)

  * **Used for:** Calculating the 3D Orbit position.
  * **Definition:** Fixed relative to the stars. The X-axis points to the Vernal Equinox.
  * **Code function:** `spice.spkpos`

### 2\. The Topocentric Frame (Topo)

  * **Used for:** Calculating Visibility (Azimuth/Elevation).
  * **Definition:** Fixed to the DSN station on Earth's surface.
      * **Z-axis:** Points "Up" (Zenith).
      * **X-axis:** Points North.
      * **Y-axis:** Points East.
  * **Code function:** `spice.spkezr` (with `ref='DSS-14_TOPO'`)

## Troubleshooting

**Error: `SPICE(NOFILESLOADED)`**

  * *Cause:* SpiceyPy cannot find the kernels listed in `jwst_meta.txt`.
  * *Fix:* Open `jwst_meta.txt` and ensure the file paths match exactly where you saved the `.bsp` and `.tls` files.

**Error: `Ephemeris data not found`**

  * *Cause:* The date range in the script (`UTC_START` / `UTC_END`) is outside the range covered by `jwst_rec.bsp` or `jwst_pred.bsp`.
  * *Fix:* Change the dates in the `__main__` block to a range covered by your kernel, or download an updated kernel.

## 6. Key SpiceyPy Functions Used

This code uses several core `spiceypy` (SPICE) functions, often referred to as **kernels**, which retrieve, convert, and calculate planetary and spacecraft geometry.

---

### A. Kernel Management and Initialization

| Function | Purpose | Input | Output |
| :--- | :--- | :--- | :--- |
| `spice.furnsh` | Loads SPICE kernels into the kernel pool. This is the **required** first step for any geometric calculation. | `jwst_meta.txt` (Meta-kernel file path) | None (Loads data into memory) |
| `spice.kclear` | Clears all kernels from the kernel pool memory. **Crucial** for running scripts multiple times. | None | None |

---

### B. Time Conversion and Handling

| Function | Purpose | Input | Output |
| :--- | :--- | :--- | :--- |
| `spice.str2et` | Converts a UTC (Universal Time Coordinated) date string into **Ephemeris Time (ET)**, also known as Barycentric Dynamical Time (TDB). SPICE calculations **must** use ET. | String (`'2025-06-01'`) | Floating-point number (ET seconds since J2000 epoch) |
| `spice.et2datetime` | Converts an ET epoch into a Python `datetime` object for plotting and display purposes. | Floating-point number (ET) | `datetime` object |

---

### C. ID and Name Mapping

| Function | Purpose | Input | Output |
| :--- | :--- | :--- | :--- |
| `spice.bodn2c` | Converts a **Body Name** (e.g., `'JWST'`, `'EARTH'`) into its corresponding NAIF Integer ID. This makes the code readable and reliable. | String (`'JWST'`) | Integer ID (`-170`) |

---

### D. Position and Geometry Calculation

These are the primary functions for determining where an object is located in space.

| Function | Purpose | Input | Output |
| :--- | :--- | :--- | :--- |
| `spice.spkpos` | Calculates the **position** (vector) of a **Target** relative to an **Observer** in a given **Reference Frame** (e.g., `'J2000'`). | `targ`, `et`, `ref`, `abcorr`, `obs` | `pos` (3-element array: X, Y, Z), `lt` (Light Time) |
| `spice.spkezr` | Calculates the **State Vector** (position and velocity) of a **Target** relative to an **Observer** in a given **Reference Frame**. This is used for DSN visibility because the velocity is implicitly needed for the light time corrections (`'LT+S'`). | `targ`, `et`, `ref`, `abcorr`, `obs` | `state` (6-element array: X, Y, Z, Vx, Vy, Vz), `lt` (Light Time) |

---

### E. Coordinate Transformation

| Function | Purpose | Input | Output |
| :--- | :--- | :--- | :--- |
| `spice.recrad` | Converts a position vector from **Rectangular** coordinates (X, Y, Z) to **Range, Azimuth, and Elevation/Latitude** (spherical coordinates). | `position_topo` (3-element array: X, Y, Z) | `r` (Range), `az_rad` (Azimuth in rad), `el_rad` (Elevation/Latitude in rad) |
| `np.deg2rad` / `np.rad2deg` | Standard NumPy functions used to convert between degrees and radians, as `spice.recrad` returns results in **radians**. | Value in degrees or radians | Converted value in radians or degrees |
