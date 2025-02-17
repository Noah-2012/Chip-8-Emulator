def create_chip8_rom(instructions, filename="chip8_rom.ch8"):
    # `instructions` ist eine Liste von Opcodes als Hex-Werte
    with open(filename, 'wb') as f:
        for instruction in instructions:
            # Jedes Element in der Liste ist ein 16-Bit-Wert (2 Bytes)
            f.write(instruction.to_bytes(2, byteorder='big'))

# Beispiel-Opcodes, die du ausführen möchtest
instructions = [
    0x6000,  # LD V0, 0x00
    0x6101,  # LD V1, 0x01
    0xA2F0,  # LD I, 0x2F0 (Startadresse für Sprites)
    0x00E0,  # CLS (Bildschirm löschen)
    0xD015   # DRW V0, V1, 5 (Sprite zeichnen)
]




create_chip8_rom(instructions)
