def ip_para_binario(ip):
    return ''.join(f'{int(octeto):08b}' for octeto in ip.split('.'))

def binario_para_ip(binario):
    return '.'.join(str(int(binario[i:i+8], 2)) for i in range(0, 32, 8))

def calcular_rede(ip, mascara):
    # Converte IP e máscara para binário
    ip_bin = ip_para_binario(ip)
    mascara_bin = '1' * mascara + '0' * (32 - mascara)
    
    # Endereço da rede (fazendo um AND entre IP e máscara)
    rede_bin = ''.join('1' if ip_bin[i] == '1' and mascara_bin[i] == '1' else '0' for i in range(32))
    endereco_rede = binario_para_ip(rede_bin)
    
    # Endereço de broadcast (fazendo um OR entre IP e o inverso da máscara)
    broadcast_bin = ''.join(ip_bin[i] if mascara_bin[i] == '1' else '1' for i in range(32))
    endereco_broadcast = binario_para_ip(broadcast_bin)
    
    # Faixa de endereços IP para hosts
    primeiro_host_bin = rede_bin[:-1] + '1'
    ultimo_host_bin = broadcast_bin[:-1] + '0'
    primeiro_host = binario_para_ip(primeiro_host_bin)
    ultimo_host = binario_para_ip(ultimo_host_bin)
    
    # Quantidade máxima de hosts
    quantidade_hosts = (2 ** (32 - mascara)) - 2  # subtrai 2 pelo endereço de rede e de broadcast
    
    # Resultados
    print(f"Endereço da rede: {endereco_rede}")
    print(f"Endereço de broadcast: {endereco_broadcast}")
    print(f"Faixa de endereços IP para hosts: {primeiro_host} - {ultimo_host}")
    print(f"Quantidade máxima de hosts: {quantidade_hosts}")

if __name__ == "__main__":
    entrada = input("Digite o endereço IP e a máscara de rede (formato IP/Máscara, ex: 192.168.1.1/24): ")
    ip, mascara = entrada.split('/')
    mascara = int(mascara)
    calcular_rede(ip, mascara)
