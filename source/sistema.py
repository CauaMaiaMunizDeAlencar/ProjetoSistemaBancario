from database import conectar

def sacar(conta_id, valor): #Define função sacar.
    conn = conectar()
    cursor = conn.cursor()

    try:
        conn.start_transaction()

        cursor.execute("SELECT saldo FROM contas WHERE id = %s FOR UPDATE", (conta_id,))
        saldo = cursor.fetchone()[0]

        if saldo >= valor:
            novo_saldo = saldo - valor
            cursor.execute("UPDATE contas SET saldo = %s WHERE id = %s", (novo_saldo, conta_id))
            conn.commit()
            print("Saque realizado")
        else:
            print("Saldo insuficiente")
            conn.rollback()
    
    except Exception as e:
        print("Erro:", e)
        conn.rollback()
    finally:
        conn.close()

def ver_saldo(conta_id): #Define função ver saldo.
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT saldo FROM contas WHERE id = %s", (conta_id,))
        resultado = cursor.fetchone()

        if resultado:
            print(f"Saldo da conta {conta_id}: R$ {resultado[0]:.2f}")
        else:
            print("Conta não encontrada!")

    except Exception as e:
        print("Erro:", e)

    finally:
        conn.close()

def depositar(conta_id, valor): #Define função depositar.
    conn = conectar()
    cursor = conn.cursor()

    try:
        conn.start_transaction()

        # trava a linha pra evitar conflito com outras threads
        cursor.execute(
            "SELECT saldo FROM contas WHERE id = %s FOR UPDATE",
            (conta_id,)
        )
        resultado = cursor.fetchone()

        if resultado:
            saldo = resultado[0]
            novo_saldo = saldo + valor

            cursor.execute(
                "UPDATE contas SET saldo = %s WHERE id = %s",
                (novo_saldo, conta_id)
            )

            conn.commit()
            print(f"Depósito realizado! Novo saldo: R$ {novo_saldo:.2f}")
        else:
            print("Conta não encontrada!")
            conn.rollback()

    except Exception as e:
        print("Erro:", e)
        conn.rollback()

    finally:
        conn.close()

    from db import conectar


def transferir(conta_origem, conta_destino, valor): #Define função transferir.
    conn = conectar()
    cursor = conn.cursor()

    try:
        conn.start_transaction()

        cursor.execute(
            "SELECT saldo FROM contas WHERE id = %s FOR UPDATE",
            (conta_origem,)
        )
        origem = cursor.fetchone()

        if not origem:
            print("Conta de origem não encontrada!")
            conn.rollback()
            return

        saldo = origem[0]

        if saldo < valor:
            print("Saldo insuficiente!")
            conn.rollback()
            return

        cursor.execute(
            "SELECT saldo FROM contas WHERE id = %s FOR UPDATE",
            (conta_destino,)
        )
        destino = cursor.fetchone()

        if not destino:
            print("Conta de destino não encontrada!")
            conn.rollback()
            return

        # Atualiza os saldos
        cursor.execute(
            "UPDATE contas SET saldo = saldo - %s WHERE id = %s",
            (valor, conta_origem)
        )

        cursor.execute(
            "UPDATE contas SET saldo = saldo + %s WHERE id = %s",
            (valor, conta_destino)
        )

        conn.commit()
        print("Transferência realizada com sucesso!")

    except Exception as e:
        conn.rollback()
        print("Erro:", e)

    finally:
        conn.close()
