# Replace Linux/AMD64 numeric constants with human readable names.
# @author b0bb
# @category Pwn
# @keybinding
# @menupath Analysis.Pwn.Constants.amd64
# @toolbar

import ghidra.app.util.opinion.ElfLoader as ElfLoader
from lib.Constants import Constants


def run():
    if currentProgram.getExecutableFormat() != ElfLoader.ELF_NAME:
        popup("Not an ELF file, cannot continue")
        return

    arch = "amd64"
    abi = "default"

    Constants(currentProgram, currentSelection, monitor, state, arch, abi)


run()
