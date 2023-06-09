
-- JOGADAS definition

CREATE TABLE JOGADAS (

chave_jogador INTEGER,

cod_peca INTEGER NOT NULL,

id_jogada INTEGER ,

posicao_init_x INTEGER NOT NULL,

posicao_init_y INTEGER NOT NULL,

pos_final_x INTEGER NOT NULL, 

pos_final_y INTEGER NOT NULL,

comentario_especialista TEXT,

chave_partida INTEGER,

chave_rival INTEGER,

CONSTRAINT JOGADAS_PK PRIMARY KEY  AUTOINCREMENT (id_jogada),

CONSTRAINT JOGADAS_FK FOREIGN KEY (chave_rival) REFERENCES PARTICIPANTES(id) ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT JOGADAS_FK_1 FOREIGN KEY (chave_jogador) REFERENCES PARTICIPANTES(id) ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT JOGADAS_FK_2 FOREIGN KEY (chave_partida) REFERENCES PARTIDA(id) ON DELETE CASCADE ON UPDATE CASCADE

);

-- PARTIDA definition

CREATE TABLE PARTIDA (

jogador_primario INTEGER NOT NULL,

jogador_secundario INTEGER NOT NULL,

arbitro INTEGER NOT NULL,

pecas_pretas INTEGER NOT NULL,

pecas_brancas INTEGER NOT NULL,

data_inicio TEXT NOT NULL,

data_fim TEXT NOT NULL,

vencedor TEXT,

id INTEGER,

chave_campeonato INTEGER,

chave_salao INTEGER,

CONSTRAINT PARTIDA_PK PRIMARY KEY (id),

CONSTRAINT PARTIDA_FK FOREIGN KEY (chave_campeonato) REFERENCES CAMPEONATO(id) ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT PARTIDA_FK_1 FOREIGN KEY (chave_salao) REFERENCES SALAO(id) ON DELETE CASCADE ON UPDATE CASCADE

);

-- PARTICIPANTE_CAMPEONATO definition

CREATE TABLE PARTICIPANTE_CAMPEONATO (

id INTEGER,

funcao TEXT NOT NULL,

chave_nacao INTEGER,

chave_partida INTEGER,

chave_participante INTEGER,

CONSTRAINT PARTICIPANTE_CAMPEONATO_PK PRIMARY KEY (id),

CONSTRAINT PARTICIPANTE_CAMPEONATO_FK FOREIGN KEY (chave_nacao) REFERENCES NACAO(id) ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT PARTICIPANTE_CAMPEONATO_FK_1 FOREIGN KEY (chave_participante) REFERENCES PARTICIPANTES(id) ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT PARTICIPANTE_CAMPEONATO_FK_2 FOREIGN KEY (chave_partida) REFERENCES PARTIDA(id) ON DELETE CASCADE ON UPDATE CASCADE

);

-- PARTICIPANTES definition

CREATE TABLE PARTICIPANTES (

numero_associado INTEGER NOT NULL,

nome TEXT NOT NULL,

endereco TEXT NOT NULL,

telefone INTEGER NOT NULL,

nivel_jogo INTEGER NOT NULL,

chave_nacao TEXT,

id INTEGER,

arbitro TEXT NOT NULL,

CONSTRAINT PARTICIPANTES_PK PRIMARY KEY (id),

CONSTRAINT PARTICIPANTES_FK FOREIGN KEY (chave_nacao) REFERENCES NACAO(id) ON DELETE CASCADE ON UPDATE CASCADE

);

-- NACAO definition

CREATE TABLE NACAO (

nome TEXT NOT NULL,

id INTEGER,

CONSTRAINT NACAO_PK PRIMARY KEY (id)

);

-- SALAO definition

CREATE TABLE SALAO (

id INTEGER,

capacidade INTEGER NOT NULL,

radio TEXT NOT NULL,

televisao TEXT NOT NULL,

video TEXT NOT NULL,

internet TEXT NOT NULL,

chave_campeonato INTEGER,

inicio_uso TEXT NOT NULL,

fim_uso INTEGER NOT NULL,

CONSTRAINT SALAO_PK PRIMARY KEY (id),

CONSTRAINT SALAO_FK FOREIGN KEY (chave_campeonato) REFERENCES CAMPEONATO(id) ON DELETE CASCADE ON UPDATE CASCADE

);

-- REGISTRO_HOSPEDAGEM definition

CREATE TABLE REGISTRO_HOSPEDAGEM (

id INTEGER,

chave_campeonato INTEGER,

momento_entrada TEXT NOT NULL,

momento_saida TEXT NOT NULL,

chave_hospedagem INTEGER,

chave_participante INTEGER,

CONSTRAINT REGISTRO_HOSPEDAGEM_PK PRIMARY KEY (id),

CONSTRAINT REGISTRO_HOSPEDAGEM_FK FOREIGN KEY (chave_campeonato) REFERENCES CAMPEONATO(id) ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT REGISTRO_HOSPEDAGEM_FK_1 FOREIGN KEY (chave_hospedagem) REFERENCES HOSPEDAGEM(id) ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT REGISTRO_HOSPEDAGEM_FK_2 FOREIGN KEY (chave_participante) REFERENCES PARTICIPANTES(id) ON DELETE CASCADE ON UPDATE CASCADE

);

-- HOSPEDAGEM definition

CREATE TABLE HOSPEDAGEM (

id INTEGER,

nome TEXT NOT NULL,

cod_postal INTEGER NOT NULL,

endereco INTEGER NOT NULL,

CONSTRAINT HOSPEDAGEM_PK PRIMARY KEY (id)

);

-- RANKING_GERAL definition

CREATE TABLE RANKING_GERAL (

nivel_jogo INTEGER NOT NULL,

id INTEGER,

vitorias INTEGER NOT NULL,

derrotas INTEGER NOT NULL,

tempo_medio_jogo NUMERIC NOT NULL,

tempo_total_jogo NUMERIC NOT NULL,

numero_jogadas INTEGER NOT NULL,

numero_partidas INTEGER NOT NULL,

chave_participante INTEGER NOT NULL,

CONSTRAINT RANKING_GERAL_PK PRIMARY KEY (id),

CONSTRAINT RANKING_GERAL_FK FOREIGN KEY (chave_participante) REFERENCES PARTICIPANTES(id) ON DELETE CASCADE ON UPDATE CASCADE

);

-- CAMPEONATO definition

CREATE TABLE CAMPEONATO (

data_inicio TEXT NOT NULL,

nome TEXT NOT NULL,

jornada TEXT NOT NULL,

id INTEGER,

CONSTRAINT CAMPEONATO_PK PRIMARY KEY (id)

);

-- RANKING_CAMPEONATO definition

CREATE TABLE RANKING_CAMPEONATO (

id INTEGER,

posicao_ranking INTEGER NOT NULL,

tempo_jogado NUMERIC NOT NULL,

chave_ranking_geral INTEGER,

tempo_medio_campeonato NUMERIC NOT NULL,

chave_participante_campeonato INTEGER,

chave_campeonato INTEGER,

CONSTRAINT RANKING_CAMPEONATO_PK PRIMARY KEY (id),

CONSTRAINT RANKING_CAMPEONATO_FK_1 FOREIGN KEY (chave_campeonato) REFERENCES CAMPEONATO(id) ON DELETE CASCADE ON UPDATE CASCADE,

CONSTRAINT RANKING_CAMPEONATO_FK_2 FOREIGN KEY (chave_participante_campeonato) REFERENCES PARTICIPANTE_CAMPEONATO(id),

CONSTRAINT RANKING_CAMPEONATO_FK FOREIGN KEY (chave_ranking_geral) REFERENCES RANKING_GERAL(id) ON DELETE CASCADE ON UPDATE CASCADE

);