import subprocess


def compile_zig():
    # Comando para compilar um arquivo Zig
    result = subprocess.run(['zig', 'build-exe', 'zigarraytest.zig'], capture_output=True, text=True)
    
    # Verifica se o comando foi executado com sucesso
    if result.returncode == 0:
        print("Compilação bem-sucedida!")
    else:
        print("Erro na compilação:")
        print(result.stderr)

if __name__ == "__main__":
    compile_zig()

