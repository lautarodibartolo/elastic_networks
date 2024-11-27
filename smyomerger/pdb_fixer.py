import sys

def add_chain_id(input_file, output_file, chain_id='A'):
    """
    Add chain ID to PDB file ATOM records while preserving exact PDB format spacing.
    
    Parameters:
    -----------
    input_file : str
        Input PDB filename
    output_file : str
        Output PDB filename
    chain_id : str
        Chain identifier to add (default: 'A')
    """
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        for line in fin:
            if line.startswith('ATOM  ') or line.startswith('HETATM'):
                # PDB format is very strict about column positions
                # We'll split the line into its components and rebuild it with proper spacing
                
                record_type = line[0:6]     # ATOM or HETATM
                atom_num = line[6:11]       # Atom serial number
                atom_name = line[11:16]     # Atom name
                alt_loc = line[16:17]       # Alternate location
                res_name = line[17:20]      # Residue name
                # Chain ID will go in column 21
                res_num = line[22:26]       # Residue sequence number
                insert_code = line[26:27]   # Insertion code
                coordinates = line[27:]      # Everything else (coordinates, etc.)
                
                # Rebuild the line with exact spacing, including the chain ID
                new_line = f"{record_type}{atom_num}{atom_name}{alt_loc}{res_name} {chain_id}{res_num}{insert_code}{coordinates}"
                fout.write(new_line)
            else:
                # Write non-ATOM lines as they are
                fout.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.pdb output.pdb")
        sys.exit(1)
    
    input_pdb = sys.argv[1]
    output_pdb = sys.argv[2]
    add_chain_id(input_pdb, output_pdb)
