# tudo em uma strig.
sqltabelas = '''
CREATE TABLE "endereco" (
    "endereco_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "endereco_status" varchar(255) NOT NULL DEFAULT 'ativo',

    "endereco_cep" varchar(255) NOT NULL,
    "endereco_rua" varchar(255),
    "endereco_numero" varchar(255),
    "endereco_complemento" varchar(255),
    "endereco_bairro" varchar(255),
    "endereco_cidade" varchar(255),
    "endereco_estado" varchar(255)
);

CREATE TABLE "registro" (
    "registro_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "registro_status" varchar(255) NOT NULL DEFAULT 'ativo',

    "registro_nome" varchar(255) NOT NULL,
    "registro_sobrenome" varchar(15) NOT NULL,
    "registro_email" varchar(255) UNIQUE,
    "registro_senha" varchar(255)    
);

CREATE TABLE "cartao" (
    "cartao_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cartao_status" varchar(255) NOT NULL DEFAULT 'ativo',

    "cartao_numero" varchar(255) NOT NULL,
    "cartao_titular" varchar(255),
    "cartao_mes" varchar(255),
    "cartao_ano" varchar(255),
    "cartao_cvv" varchar(255)    
);
CREATE TABLE "produto" (
    "produto_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "produto_status" varchar(255) NOT NULL DEFAULT 'ativo',

    "produto_nome" varchar(255) NOT NULL,
    "produto_potencia" varchar(255),
    "produto_preco" varchar(255)
);

CREATE TABLE "sistema" (
    "sistema_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "sistema_status" varchar(255) NOT NULL DEFAULT 'ativo',
    "sistema_escolha_usuario" varchar(255) NOT NULL,
    
    "sistema_kwhrdia" varchar(255),
    "sistema_energiasol" varchar (255),
    "sistema_estado" varchar(255),
    "sistema_cidade" varchar(255),
    
    "sistema_bateriavolts" varchar(255),
    "sistema_energiadiareserva" varchar(255),
    
    "sistema_paineltipo" varchar(255),
    "sistema_modulowatt" varchar(255),

    "sistema_temperaturaopcao" varchar(255),
    "sistema_perdasinversor" varchar(255),
    "sistema_fatorsegurancainversor" varchar(255),
    "sistema_perdascabo" varchar(255),
    "sistema_perdasincompatibilidade" varchar(255),
    "sistema_perdassujeira" varchar(255),
    "sistema_profundidade" varchar(255),
    "sistema_bateriaeficiencia" varchar(255)
);
  
CREATE TABLE "pedido" (
    "pedido_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "pedido_status" varchar(255) NOT NULL DEFAULT 'ativo',
    
    "pedido_registro" int,
    "pedido_endereco" int,
    "pedido_sistema" int,
    "pedido_cartao" int,
    "pedido_produto" int,
        
        CONSTRAINT fk_endereco
            FOREIGN KEY ("pedido_endereco")
            REFERENCES "endereco"("endereco_id"),
        CONSTRAINT fk_registro
            FOREIGN KEY ("pedido_registro")
            REFERENCES "registro"("registro_id"),
        CONSTRAINT fk_sistema
            FOREIGN KEY ("pedido_sistema")
            REFERENCES "sistema"("sistema_id"),
        CONSTRAINT fk_cartao
            FOREIGN KEY ("pedido_cartao")
            REFERENCES "cartao"("cartao_id"),
        CONSTRAINT fk_produto
            FOREIGN KEY ("pedido_produto")
            REFERENCES "produto"("produto_id")
);

-- //////////////////////////////////////////////////////////////////////////
-- /////////////////////////////////////////////////////////////////////////
-- ////////////////////tabelas por enquanto desativadas./////////////////////
-- 
-- CREATE TABLE "orcamento" (
--     "orcamento_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     "cliente_id" int,
--     "orcamento_media_energia" decimal (10,2),
--     "orcamento_media_pagamento_energia" decimal (10,2),
--     "orcamento_tipo_residencia" varchar(255),
--     "orcamento_valor_instalacao" decimal (10,2),
--     "orcamento_data" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     "orcamento_status" varchar(255) NOT NULL DEFAULT 'ativo',
--         CONSTRAINT fk_cliente
--             FOREIGN KEY ("cliente_id")
--             REFERENCES "cliente"("cliente_id")
-- );


-- CREATE TABLE "pagamento" (
--     "pagamento_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     "cartao_id" int,
--     "pagamento_forma" varchar(255),
--     "pagamento_valor" decimal (10,2),
--     "pagamento_Bandeira_cartao" varchar(255),
--     "banco_id" int,
--     "pagamento_descricao" varchar(255),
--     "pagamento_status" varchar(255) NOT NULL DEFAULT 'ativo',
--         CONSTRAINT fk_cartao
--             FOREIGN KEY ("cartao_id")
--             REFERENCES "cartao"("cartao_id"),
--         CONSTRAINT fk_banco
--             FOREIGN KEY ("banco_id")
--             REFERENCES "banco"("banco_id")
-- );

'''