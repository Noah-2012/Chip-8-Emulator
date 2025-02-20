# Chip-8-Emulator
An Emulator for Chip 8 Games or Programms written in python.

## Start

To start a .ch8 file you have to enter the following:

```bash
python emulator.py <file> [-t] <tickrate> [-ep] <entrypoint>
```

With `-t <tickrate>` you can specify your own tickrate. The default is 500.
With `-ep <entrypoint>` you can specify your own entrypoint with e. g. `0x100` and `0x200` is the default.

## Steering

- `SPACE` is for pause and play.
- If it is paused you can do Steps with `s`.
- With `TAB` you can restart the script.
- With `l` you can quit.

## Movement

This are the keys to move and interact with programms: `1, 2, 3, 4, q, w, e, r, a, s, d, f, z, x, c, v`.
