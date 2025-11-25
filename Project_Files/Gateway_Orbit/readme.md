# Tutorial: Gateway Near Rectilinear Halo Orbit (NRHO) Orbit Visualization with SpiceyPy

## Overview

This tutorial walks through how to use **SpiceyPy** (the Python interface to NASA's SPICE toolkit) to visualize the **Gateway Near Rectilinear Halo Orbit (NRHO)** in multiple reference frames. Using the provided Python scripts, you will generate three distinct views of the Gateway spacecraft trajectory:

- **Sun‑Centered Inertial (SCI/J2000)**
- **Earth‑Centered Inertial (ECI/J2000)**
- **Moon‑Centered Rotating Earth–Moon Frame**

**Key Concepts Covered:**

- Loading and managing SPICE kernels (meta-kernel setup)
- Interpreting time using UTC to ET conversions
- Computing state vectors in different frames
- Constructing and using a rotating coordinate frame
- Visualizing multi-body trajectories in 3D

---

## 1. Prerequisites

Ensure you have Python 3.7+ installed. Install required packages:

```bash
pip install spiceypy numpy matplotlib
```

---

## 2. Project Structure & Setup

SPICE requires external data files called **kernels**. These contain ephemerides, time constants, planetary constants, etc. Your scripts will not run unless these kernels are available and properly listed in the meta-kernel.

A recommended directory layout is:

```
your_project/
  gateway_meta.txt
  Gateway_Orbit_SCI.py
  Gateway_Orbit_ECI.py
  Gateway_Orbit.py
  kernels/
    ... SPK, PCK, LSK files ...
```

### Step A: Required Kernels
Your `gateway_meta.txt` must point to the following kernel types:
- **Leap seconds kernel** (e.g., `naif0012.tls`)
- **Planetary ephemeris** (e.g., `de440.bsp`)
- **Moon and Earth constants** (e.g., `pck00010.tpc`)
- **Gateway NRHO SPK** (your spacecraft trajectory file), using NAIF ID `-60000`

### Step B: The Meta-Kernel (`gateway_meta.txt`)
This file tells SPICE which kernels to load. A gateway_meta-kernel looks like:

```text
\begindata

   KERNELS_TO_LOAD = (
      'naif0012.tls',
      'de440.bsp',
      'pck00010.txt',
      'receding_horiz_3189_1burnApo_DiffCorr_15yr.bsp'
   )

\enddata
```

> Ensure file paths in this meta-kernel match your local directory structure.

---

## 3. Running the Orbit Visualization Scripts

Run each script individually:

```bash
python Gateway_Orbit_SCI.py
python Gateway_Orbit_ECI.py
python Gateway_Orbit.py
```

Each script:
- Loads SPICE kernels
- Computes Gateway, Earth, and Moon state vectors
- Creates a 3D plot
- Clears the kernel pool using `spice.kclear()`

---

## 4. Understanding the Output

Each script generates a specific geometric visualization.

### A. Sun‑Centered Inertial (SCI/J2000) — `Gateway_Orbit_SCI.py`
**What it shows:**
- Gateway, Earth, and Moon trajectories around the Sun
- A second, zoomed‑in subplot centered on Earth showing the Moon and NRHO in SCI-frame coordinates

**Frame:** `J2000`, observer = Sun

This is your *solar‑system context* view.

---

### B. Earth‑Centered Inertial (ECI/J2000) — `Gateway_Orbit_ECI.py`
**What it shows:**
- Earth at the origin
- Moon’s orbit
- Gateway’s NRHO in an inertial Earth‑centered frame

**Frame:** `J2000`, observer = Earth

This is the traditional Earth‑relative spacecraft dynamics view.

---

### C. Moon‑Centered Rotating Frame — `Gateway_Orbit.py`
**What it shows:**
- A Moon‑centered view where the x‑axis always points from Moon → Earth
- The NRHO plotted in the Y–Z plane
- A clean “halo” shape showing the lunar polar loop

**Frame:** Rotating frame constructed using instantaneous Earth–Moon geometry.

This is the most intuitive visual representation of the NRHO geometry.

---

## 5. Technical Explanation: Coordinate Frames

### 1. Inertial J2000 Frame
Used for SCI and ECI visualizations.

- Fixed relative to background stars
- Used to compute Gateway/Earth/Moon state vectors via:
  - `spice.spkezr`

### 2. Custom Earth–Moon Rotating Frame
Constructed manually in `Gateway_Orbit.py`:

- **x-axis:** Moon to Earth direction
- **z-axis:** orbital angular momentum (cross-product of Earth–Moon position & velocity)
- **y-axis:** completes right-handed coordinate system

Gateway and Earth vectors are rotated into this frame before plotting.

---

## 6. Troubleshooting

### **Error: `SPICE(NOFILESLOADED)`**
**Cause:** SPICE couldn't find the kernels listed in `gateway_meta.txt`.

**Fix:**
- Ensure the meta-kernel is in the same directory where you run the scripts.
- Verify that all paths in `gateway_meta.txt` are correct.

### **Error: `SPICE(SPKINSUFFDATA)`**
**Cause:** The chosen UTC time window is outside the coverage of your kernels.

**Fix:**
- Adjust the `utc_start` and `utc_end` variables in the scripts.
- Use SPKs with a broader time range if needed.

### **Plot appears empty or distorted**
- Check that NAIF IDs (Earth, Moon, Gateway) match your kernels
- Verify your meta-kernel loads all required SPKs

---

## 7. Key SpiceyPy Functions Used

### A. Kernel Management
| Function | Purpose |
|---------|---------|
| `spice.furnsh` | Load kernels from meta-kernel |
| `spice.kclear` | Clear kernel pool |

### B. Time Conversion
| Function | Purpose |
|---------|---------|
| `spice.str2et` | Convert UTC → ET |

### C. Position & State Computation
| Function | Purpose |
|---------|---------|
| `spice.spkezr` | Compute position + velocity of a target relative to an observer |

### D. Coordinate Transformation
| Function | Purpose |
|---------|---------|
| Manual rotation matrix | Used in Moon‑centered rotating frame construction |

