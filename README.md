# N722BD flight and weather replay

An offline 3D visualization of the November 1, 2026 flight, using the supplied Flightradar24 observations, interpolated KAMX radar reflectivity, and USGS ground imagery/elevation. Includes time-linked ATC excerpts, an estimated terminal trajectory, speed and kinetic-energy displays, and an adjustable stabilizer-loss scenario.

## Open

Download this repository and open **index.html** in a modern browser with WebGL and DecompressionStream support. The HTML embeds its data and JavaScript; no server, audio, or network requests are required. GitHub's file viewer displays HTML source; download the file to run it.

## Interpretation

- White shows the sampled trajectory through the last changing altitude observation at 17:49:22.955 UTC. Amber estimates height thereafter; horizontal positions remain recorded through 17:49:31.540. The final curve reaches a published estimated site near 26.63295 N, 80.11301 W around 17:49:34. This is one illustrative scenario, not a verified impact time or surveyed location.
- The jet points along the local 3D path tangent. This is not measured pitch, bank or angle of attack.
- Stabilizer loss is accepted as a scenario assumption. Its adjustable default, 17:49:03 UTC, is the best segmented altitude-fit transition. Neither that time nor a causal contribution is uniquely identified. The earlier-trend comparison is not an intact-aircraft aerodynamic simulation.
- Energy uses an adjustable assumed constant moving mass (default 8,000 kg), excluding fuel combustion energy. Ground-relative speed is not airspeed; kinetic energy is not impact force or structural stress.
- Radar contours are interpolated reflectivity, not measured cloud boundaries. Default states use only already-acquired gates; the alternative event-volume view labels later rays. Spatial coverage and temporal sampling limit interpretation.
- ATC alignment is provisional. The supplied conference transcript is included verbatim and has not been independently authenticated. Its approximate crash time differs from the flight-data model clock.

Full sources and methods are available in the replay's **Sources & interpretation** dialog.

## Reproduce

Build the identical standalone HTML from the prepared payload:

```sh
python3 build_animation.py
```

Rebuild the scenario and radar surfaces from the included prepared inputs:

```sh
python3 -m pip install -r requirements.txt
python3 extend_impact.py
python3 stabilizer_analysis.py
python3 radar_volume.py
python3 build_animation.py
```

The prepared animation input contains extracted radar gates. This repository does not include the original Level-II radar archive. The generated `volume_data.json` is ignored because its contents are already represented in the compressed payload.

Run the headless playback-logic check with Node 18+:

```sh
node check_logic.cjs
```

This checks syntax, timeline bounds, energy scaling and transcript seeking with WebGL deliberately unavailable. Final WebGL appearance has not been verified in the latest environment.

## Sources and third-party materials

Flight observations: supplied Flightradar24 granular CSV. Radar: NOAA NEXRAD KAMX Level-II via Unidata archive. Ground: USGS NAIP Plus and 3DEP. Geometry rendering: Three.js r170 and OrbitControls (MIT notices retained in their source). ATC excerpts and public geolocation sources are linked within the HTML. The user-supplied NTSB conference transcript is preserved in `animation_sources/ntsb_conference_supplied.txt`.

Third-party data and text retain their respective rights and attribution requirements; this import does not relicense them.
