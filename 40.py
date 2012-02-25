import string

ir_str=string.join([str(i) for i in range(1,1000001)], "")
print int(ir_str[0])*int(ir_str[9])*int(ir_str[99])*int(ir_str[999])*int(ir_str[9999])*int(ir_str[99999])*int(ir_str[999999])
