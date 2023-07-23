#EJERCICIO 1


def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


m = bytes.fromhex("B1EF2ACFE2BAEEFF")
k = bytes.fromhex("91BA13BA21AABB12")

print(xor_data(m,k).hex())

def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


m = bytes.fromhex("B1EF2ACFE2BAEEFF")
k = bytes.fromhex("B98A15BA31AEBB3F")

print(xor_data(m,k).hex())