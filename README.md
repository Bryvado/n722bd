# N722BD flight and weather replay

Open `index.html` from a downloaded copy of the whole repository, or serve this directory with any static web server. Keep the `assets` directory beside the HTML. The launcher reconstructs the original standalone replay from compressed script assets; no build step is required to view it. A modern browser with WebGL and DecompressionStream is required.

The replay includes recorded flight observations, interpolated NEXRAD radar, USGS aerial imagery and elevation, time-linked ATC excerpts, estimated terminal motion and kinetic energy, and an adjustable stabilizer-loss scenario. It contains no audio or impact effects.

## Scientific limits

White denotes sampled position and altitude through 17:49:22.955 UTC; amber estimates height after that point. Recorded positions continue through 17:49:31.540. The final curve to a published estimated location near 26.63295 N, 80.11301 W and contact around 17:49:34 are illustrative estimates.

The model pitches along the path tangent, not measured attitude. Assumed stabilizer loss defaults to 17:49:03, based on a segmented altitude fit; this is not a uniquely identified separation time. The trend comparison does not isolate a causal effect. Energy uses adjustable assumed mass, excluding fuel combustion. Ground-relative speed is not airspeed, and kinetic energy is not impact force.

Radar shells represent interpolated reflectivity rather than measured cloud boundaries. Default frames use already-acquired observations. ATC alignment and the user-supplied conference transcript remain provisional. Full methods, sources, and transcript appear inside the replay.

## Original files and reproducible sources

- [Standalone HTML](https://chatgpt.com/library?file_id=libfile_7aa25dd9c0548191b115796a877f24e7&account_id=personal)
- [Analysis and source package](https://chatgpt.com/library?file_id=libfile_6dadff025dc0819199be17dcccbf92ad&account_id=personal)

Those links require access to the owner's ChatGPT Library. The public repository itself contains all assets needed to view the replay.

`manifest.json` records the bundled HTML SHA-256. To reconstruct the standalone file locally, run `python3 reconstruct.py`; this uses Python's standard library only.

## Validation and attribution

The original replay passed script syntax, timeline, energy-scaling, transcript-seeking and orientation calculations. Final WebGL appearance was not verified in the latest environment.

Flight data: supplied Flightradar24 CSV. Radar: NOAA NEXRAD KAMX via Unidata. Ground: USGS NAIP Plus and 3DEP. Renderer: Three.js r170 and OrbitControls, with MIT notices embedded. Other source links and the supplied transcript are retained inside the HTML. Third-party materials retain their respective rights; this import does not relicense them.
