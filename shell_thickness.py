allowable_stresses = {'SS316': {'30' : 1321 , '70' : 1321 , '100' : 1318 , '150' : 1293 , '200' : 1274 , '250' : 1266 , '300' : 1214 } , 
                    'SS304' : {'30' : 1321 , '70' : 1281 , '100' : 1241 , '150' : 1166 , '200' : 1141 , '250' : 1121 , '300' : 1117 } , 
                    'IS2062' : {'30' : 1050 , '70' : 1050 , '100' : 1041 , '150' : 973 , '200' : 892 , '250' : 762 , '300' : 692 } , 
                    'SA516GR60': {'30' : 1054.63 , '70' : 1054.63 , '100' : 1054.63 , '150' : 1054.63 , '200' : 1054 , '250' : 1054 , '300' : 1054 }}
class shell:
    def thickness (design_pressure, shell_inside_redius, allowable_stress, joint_efficiency_factor, corrosion_allowance):
        thk = ((design_pressure*shell_inside_redius)/((allowable_stress*joint_efficiency_factor)-(0.6*design_pressure)))+(corrosion_allowance)
        return thk    
design_pressure = float(input('Design Pressur in psi = '))
shell_inside_redius = float(input('Shell inside radius in cm = '))
material_used = input('Material ASME Code (All caps , without speaces) = ')
design_tempreture = input('Design Tempreture in degree Celcious = ')
allowable_stress = int(allowable_stresses[material_used] [design_tempreture])
print('allowable stress = ' , allowable_stress )
joint_efficiency_factor = float(input('Joint Efficiency Fctor = '))
corrosion_allowance = float(input('Corrosion Allowance = '))

print('Shell Thickness = ' , shell.thickness(design_pressure, shell_inside_redius, allowable_stress, joint_efficiency_factor, corrosion_allowance) , 'mm')
