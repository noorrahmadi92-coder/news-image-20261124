// The World in One Day — Tuesday, 24 November 2026 (Node 22, stdlib only).
// The image is entry.png beside this file, drawn by draw.py (Pillow) from
// the six verified stories in the research notes: Nvidia reinstates Jensen
// Huang as CEO, Russian jets trigger a shelter alert off Ulleung Island,
// Iran steps up strikes as the US blockade bites, NATO sends an AWACS jet
// to Poland, the EU proposes a 22nd sanctions package, and the Odesa
// blackout, Vanuatu quake and Gaza strikes. This program copies the image
// to /output/entry.png and checks its PNG magic before writing.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const src = new URL('./entry.png', import.meta.url);
const data = readFileSync(src);
if (data.length < 8 || data[0] !== 0x89 || data[1] !== 0x50 ||
    data[2] !== 0x4e || data[3] !== 0x47) {
  throw new Error('entry.png is not a PNG file');
}
copyFileSync(src, join(outDir, 'entry.png'));
console.log(`Wrote ${join(outDir, 'entry.png')} (${data.length} bytes)`);
