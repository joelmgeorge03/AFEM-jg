

from afem.exchange import ImportVSP

vsp_import = ImportVSP('wingbox_test.stp')
#print(type(vsp_import))
#print(dir(vsp_import))

print(vsp_import.num_bodies)
print(vsp_import.all_bodies)

wing = vsp_import.all_bodies[0]
print(wing.name)
