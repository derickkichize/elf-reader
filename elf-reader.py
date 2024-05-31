#!/usr/bin/env python3

import struct
import sys

def read_elf_header_X86(filename):
    elf_header = {}

    try:
        with open (filename, "rb") as f:
           elf_header_data = f.read(52)
           
           (
              e_ident,
              e_type,
              e_machine,
              e_version,
              e_entry,
              e_phoff,
              e_shoff,
              e_flags,
              e_ehsize,
              e_phentsize,
              e_phnum,
              e_shentsize,
              e_shnum,
              e_shstrndx
           ) = struct.unpack("16sHHIIIIIHHHHHH", elf_header_data)

           elf_header['e_ident']     = e_ident
           elf_header['e_type']      = e_type
           elf_header['e_machine']   = e_machine
           elf_header['e_version']   = e_version
           elf_header['e_entry']     = e_entry
           elf_header['e_phoff']     = e_phoff
           elf_header['e_shoff']     = e_shoff
           elf_header['e_flags']     = e_flags
           elf_header['e_ehsize']    = e_ehsize
           elf_header['e_phentsize'] = e_phentsize
           elf_header['e_phnum']     = e_phnum
           elf_header['e_shentsize'] = e_shentsize
           elf_header['e_shnum']     = e_shnum
           elf_header['e_shstrndx']  = e_shstrndx

    except FileNotFoundError:
        print("Arquivo não encontrado:", filename)
        return None
    
    return elf_header

def read_elf_header(filename):
    elf_header = {}

    try:
        with open (filename, "rb") as f:
            elf_header_data = f.read(64)
            
            (
                e_ident,
                e_type,
                e_machine,
                e_version,
                e_entry,
                e_phoff,
                e_shoff,
                e_flags,
                e_ehsize,
                e_phentsize,
                e_phnum,
                e_shentsize,
                e_shnum,
                e_shstrndx
            ) = struct.unpack("16sHHIQQQIHHHHHH", elf_header_data)
            
            elf_header['e_ident']     = e_ident
            elf_header['e_type']      = e_type
            elf_header['e_machine']   = e_machine
            elf_header['e_version']   = e_version
            elf_header['e_entry']     = e_entry
            elf_header['e_phoff']     = e_phoff
            elf_header['e_shoff']     = e_shoff
            elf_header['e_flags']     = e_flags
            elf_header['e_ehsize']    = e_ehsize
            elf_header['e_phentsize'] = e_phentsize
            elf_header['e_phnum']     = e_phnum
            elf_header['e_shentsize'] = e_shentsize
            elf_header['e_shnum']     = e_shnum
            elf_header['e_shstrndx']  = e_shstrndx

    except FileNotFoundError:
        print("Arquivo não encontrado:", filename)
        return None
    
    return elf_header

def print_elf_header(header):
    """Function to print ELF header"""
    print("e_ident[EI_MAG]:",        header['e_ident'][:4].hex())
    print("e_ident[EI_CLASS]:",      header['e_ident'][4])
    print("e_ident[EI_DATA]:",       header['e_ident'][5])
    print("e_ident[EI_VERSION]:",    header['e_ident'][6])
    print("e_ident[EI_OSABI]:",      header['e_ident'][7])
    print("e_ident[EI_ABIVERSION]:", header['e_ident'][8])
    print("e_ident[EI_PAD]:",        header['e_ident'][9])
    print("e_type:",      header['e_type'])
    print("e_machine:",   format(header['e_machine'], '02x'))
    print("e_version:",   header['e_version'])
    print("e_entry:",     format(header['e_entry'], '02x'))
    print("e_phoff:",     header['e_phoff'])
    print("e_shoff:",     header['e_shoff'])
    print("e_flags:",     header['e_flags'])
    print("e_ehsize:",    header['e_ehsize'])
    print("e_phentsize",  header['e_phentsize'])
    print("e_phnum:",     header['e_phnum'])
    print("e_shentsize:", header['e_shentsize'])
    print("e_shnum:",     header['e_shnum'])
    print("e_shstrndx:",  header['e_shstrndx'])

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <elf_file>".format(sys.argv[0]))
        return
    
    filename = sys.argv[1]
    header = read_elf_header(filename)
    
    if header:
        print_elf_header(header)
    else:
        print("Error while reading ELF header from file:", filename)

        
if __name__ == "__main__":
    main()
