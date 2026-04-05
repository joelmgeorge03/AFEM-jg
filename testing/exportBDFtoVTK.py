
from pyNastran.bdf.bdf import BDF

def bdf_to_vtk(bdf_filename, vtk_filename):
    bdf = BDF()
    bdf.read_bdf(bdf_filename, validate=False, punch=True, xref=False)

    # --- Nodes ---
    node_ids = sorted(bdf.nodes.keys())
    node_index_map = {nid: i for i, nid in enumerate(node_ids)}

    points = [bdf.nodes[nid].get_position() for nid in node_ids]

    # --- Elements (only shells for now) ---
    cells = []
    cell_types = []

    for elem in bdf.elements.values():
        if elem.type == 'CQUAD4':
            conn = [node_index_map[nid] for nid in elem.node_ids]
            cells.append(conn)
            cell_types.append(9)  # VTK_QUAD

        elif elem.type == 'CTRIA3':
            conn = [node_index_map[nid] for nid in elem.node_ids]
            cells.append(conn)
            cell_types.append(5)  # VTK_TRIANGLE

        # You can extend this for beams/solids if needed

    # --- Write VTK ---
    with open(vtk_filename, 'w') as f:
        f.write('# vtk DataFile Version 3.0\n')
        f.write('BDF Mesh\n')
        f.write('ASCII\n')
        f.write('DATASET UNSTRUCTURED_GRID\n')

        # Points
        f.write(f'POINTS {len(points)} float\n')
        for p in points:
            f.write(f'{p[0]} {p[1]} {p[2]}\n')

        # Cells
        total_size = sum(len(c) + 1 for c in cells)
        f.write(f'\nCELLS {len(cells)} {total_size}\n')
        for c in cells:
            f.write(f'{len(c)} ' + ' '.join(map(str, c)) + '\n')

        # Cell types
        f.write(f'\nCELL_TYPES {len(cell_types)}\n')
        for ct in cell_types:
            f.write(f'{ct}\n')

    print(f"VTK file written to {vtk_filename}")


# --- Run it ---
#bdf_to_vtk('wingbox_AFEM_clean.bdf', 'wingbox.vtk')
bdf_to_vtk('supersonic.bdf', 'supersonic_test.vtk')