import streamlit as st
import boto3
import os

def aws_s3():
    st.subheader("Valida Acesso AWS S3")

    access_key = st.text_input("Access Key")
    secret_key = st.text_input("Secret Key")
    bucket_name = st.text_input("Bucket")
    bucket_pasta = st.text_input("Pasta/arquivo")
    tipo = st.selectbox("Escolha o Tipo de Operação", ["Listar Objetos", "Download de Objetos"])

    enviar = st.button("Enviar")

    if enviar:
        if tipo == "Listar Objetos":
            s3 = boto3.client(
                service_name='s3',
                region_name='us-east-1',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key       
            )

            response=s3.list_objects(Bucket=bucket_name, Prefix=bucket_pasta)
            for obj in response.get('Contents', []):
                st.write(obj["Key"])
                st.write(os.path.basename(obj["Key"]))

        if tipo == "Download de Objetos":
            s3 = boto3.client(
                service_name='s3',
                region_name='us-east-1',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key       
            )

            # Especifique o nome do arquivo local onde deseja salvar o objeto
            st.write("Iniciando Download do arquivo" + os.path.basename(bucket_pasta))
            nome_arquivo = os.path.basename(bucket_pasta)
            local_file_path = f'./arquivos/{nome_arquivo}'
            # Baixe o objeto do S3
            s3.download_file(bucket_name, bucket_pasta, local_file_path)

            with open(local_file_path, "rb") as file:
                btn = st.download_button(
                        label="Download",
                        data=file,
                        file_name=nome_arquivo
                    )


    