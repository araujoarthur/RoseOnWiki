CREATE TABLE accounts(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(30),
    password VARCHAR(110),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL,
    allowance INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE page_types(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

INSERT INTO page_types(name) VALUES('guia');
INSERT INTO page_types(name) VALUES('quest');
INSERT INTO page_types(name) VALUES('npc');
INSERT INTO page_types(name) VALUES('item');

CREATE TABLE status_types(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL
);

INSERT INTO status_types(name) VALUES('Força');
SET @str_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Destreza');
SET @dex_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Inteligência');
SET @int_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Concentração');
SET @con_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Charme');
SET @cha_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Sensibilidade');
SET @sen_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Poder de Ataque');
SET @atqpow_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Defesa');
SET @def_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Defesa Mágica');
SET @magres_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Precisão');
SET @prec_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Crítico');
SET @cri_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Esquiva');
SET @eva_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Velocidade de Ataque');
SET @atkspd_id = LAST_INSERT_ID();
INSERT INTO status_types(name) VALUES('Velocidade de Movimento');
SET @movspd_id = LAST_INSERT_ID();

CREATE TABLE item_types(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(70) NOT NULL UNIQUE
);


INSERT INTO item_types(name) VALUES('arma');
SET @arma_id = LAST_INSERT_ID();
INSERT INTO item_types(name) VALUES('escudo');
SET @escudo_id = LAST_INSERT_ID();
INSERT INTO item_types(name) VALUES('mascara');
SET @mascara_id = LAST_INSERT_ID();
INSERT INTO item_types(name) VALUES('costas');
SET @costas_id = LAST_INSERT_ID();
INSERT INTO item_types(name) VALUES('armadura');
SET @armadura_id = LAST_INSERT_ID();
INSERT INTO item_types(name) VALUES('joia');
SET @joia_id = LAST_INSERT_ID();
INSERT INTO item_types(name) VALUES('material');
SET @material_id = LAST_INSERT_ID();
INSERT INTO item_types(name) VALUES('consumivel');
SET @consumivel_id = LAST_INSERT_ID();

CREATE TABLE item_subtype(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(70) NOT NULL,
    item_type_id INTEGER NOT NULL,

    FOREIGN KEY (item_type_id) REFERENCES item_types(id)
);

INSERT INTO item_subtype(name, item_type_id) VALUES('Arco', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Espada Dupla', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Canhão', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Lança', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Arma de Impacto Uma Mão', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Machado Duas Mãos', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Espada Uma Mão', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Pistola', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Cajado', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Varinha Mágica', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Espada Duas Mãos', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Katar', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Besta', @arma_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Varinha Mágica', @arma_id);

INSERT INTO item_subtype(name, item_type_id) VALUES('Escudo', @escudo_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Recreativa', @escudo_id);

INSERT INTO item_subtype(name, item_type_id) VALUES('Óculos', @mascara_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Máscara', @mascara_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Etc', @mascara_id);

INSERT INTO item_subtype(name, item_type_id) VALUES('Escudo de Costas', @costas_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Asa', @costas_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Mochila', @costas_id);

INSERT INTO item_subtype(name, item_type_id) VALUES('Chapéu Mágico', @armadura_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Chapéu Fantasia', @armadura_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Chapéu Comum', @armadura_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Chapéu', @armadura_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Acessório Cabelos', @armadura_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Elmo', @armadura_id);

INSERT INTO item_subtype(name, item_type_id) VALUES('Anel', @joia_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Colar', @joia_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Brinco', @joia_id);

INSERT INTO item_subtype(name, item_type_id) VALUES('Cupom de Tempo', @consumivel_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Item Mágico', @consumivel_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Broca', @consumivel_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Sacador', @consumivel_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Ferramenta de Reparos', @consumivel_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Livro de Habilidades', @consumivel_id);

INSERT INTO item_subtype(name, item_type_id) VALUES('Gema', @material_id);
SET @gem_id = LAST_INSERT_ID();
INSERT INTO item_subtype(name, item_type_id) VALUES('Químico', @material_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Metal Alienígena', @material_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Metal', @material_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Couro', @material_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Material', @material_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Material de Pedra', @material_id);
INSERT INTO item_subtype(name, item_type_id) VALUES('Material de Madeira', @material_id);

CREATE TABLE weapons_data(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type_id INTEGER NOT NULL DEFAULT @arma_id,
    subtype_id INTEGER DEFAULT NULL,
    name VARCHAR(70) NOT NULL,
    attack_power REAL NOT NULL,
    accuracy REAL NOT NULL,
    attack_speed REAL NOT NULL,
    attack_range REAL NOT NULL,
    status1_id INTEGER DEFAULT NULL,
    status1_val INTEGER DEFAULT NULL,
    status2_id INTEGER DEFAULT NULL,
    status2_val INTEGER DEFAULT NULL,
    status3_id INTEGER DEFAULT NULL,
    status3_val INTEGER DEFAULT NULL,

    FOREIGN KEY (subtype_id) REFERENCES item_subtype(id),
    FOREIGN KEY (status1_id) REFERENCES status_types(id),
    FOREIGN KEY (status2_id) REFERENCES status_types(id),
    FOREIGN KEY (status3_id) REFERENCES status_types(id)

);

CREATE TABLE shield_data(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type_id INTEGER  NOT NULL DEFAULT @escudo_id,
    subtype_id INTEGER DEFAULT NULL,
    name VARCHAR(70) NOT NULL,
    defense_power REAL NOT NULL,
    evasion REAL NOT NULL,
    magical_resistence REAL NOT NULL,
    status1_id INTEGER DEFAULT NULL,
    status1_val INTEGER DEFAULT NULL,
    status2_id INTEGER DEFAULT NULL,
    status2_val INTEGER DEFAULT NULL,
    status3_id INTEGER DEFAULT NULL,
    status3_val INTEGER DEFAULT NULL,

    FOREIGN KEY (subtype_id) REFERENCES item_subtype(id),
    FOREIGN KEY (status1_id) REFERENCES status_types(id),
    FOREIGN KEY (status2_id) REFERENCES status_types(id),
    FOREIGN KEY (status3_id) REFERENCES status_types(id)
);

CREATE TABLE mask_data(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type_id INTEGER  NOT NULL DEFAULT @mascara_id,
    subtype_id INTEGER DEFAULT NULL,
    name VARCHAR(70) NOT NULL,
    defense_power REAL NOT NULL,
    evasion REAL NOT NULL,
    magical_resistence REAL NOT NULL,
        status1_id INTEGER DEFAULT NULL,
    status1_val INTEGER DEFAULT NULL,
    status2_id INTEGER DEFAULT NULL,
    status2_val INTEGER DEFAULT NULL,
    status3_id INTEGER DEFAULT NULL,
    status3_val INTEGER DEFAULT NULL,

    FOREIGN KEY (subtype_id) REFERENCES item_subtype(id),
    FOREIGN KEY (status1_id) REFERENCES status_types(id),
    FOREIGN KEY (status2_id) REFERENCES status_types(id),
    FOREIGN KEY (status3_id) REFERENCES status_types(id)
);

CREATE TABLE backshield_data(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type_id INTEGER  NOT NULL DEFAULT @costas_id,
    subtype_id INTEGER DEFAULT NULL,
    name VARCHAR(70) NOT NULL,
    defense_power REAL NOT NULL,
    evasion REAL NOT NULL,
    magical_resistence REAL NOT NULL,
    status1_id INTEGER DEFAULT NULL,
    status1_val INTEGER DEFAULT NULL,
    status2_id INTEGER DEFAULT NULL,
    status2_val INTEGER DEFAULT NULL,
    status3_id INTEGER DEFAULT NULL,
    status3_val INTEGER DEFAULT NULL,

    FOREIGN KEY (subtype_id) REFERENCES item_subtype(id),
    FOREIGN KEY (status1_id) REFERENCES status_types(id),
    FOREIGN KEY (status2_id) REFERENCES status_types(id),
    FOREIGN KEY (status3_id) REFERENCES status_types(id)
);

CREATE TABLE armor_data(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type_id INTEGER  NOT NULL DEFAULT @armadura_id,
    subtype_id INTEGER DEFAULT NULL,
    name VARCHAR(70) NOT NULL,
    defense_power REAL NOT NULL,
    evasion REAL NOT NULL,
    magical_resistence REAL NOT NULL,
    status1_id INTEGER DEFAULT NULL,
    status1_val INTEGER DEFAULT NULL,
    status2_id INTEGER DEFAULT NULL,
    status2_val INTEGER DEFAULT NULL,
    status3_id INTEGER DEFAULT NULL,
    status3_val INTEGER DEFAULT NULL,

    FOREIGN KEY (subtype_id) REFERENCES item_subtype(id),
    FOREIGN KEY (status1_id) REFERENCES status_types(id),
    FOREIGN KEY (status2_id) REFERENCES status_types(id),
    FOREIGN KEY (status3_id) REFERENCES status_types(id)
);

CREATE TABLE jewel_data(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type_id INTEGER  NOT NULL DEFAULT @joia_id,
    subtype_id INTEGER DEFAULT NULL,
    name VARCHAR(70) NOT NULL,
    quality INTEGER NOT NULL,
    status1_id INTEGER DEFAULT NULL,
    status1_val INTEGER DEFAULT NULL,
    status2_id INTEGER DEFAULT NULL,
    status2_val INTEGER DEFAULT NULL,
    status3_id INTEGER DEFAULT NULL,
    status3_val INTEGER DEFAULT NULL,

    FOREIGN KEY (subtype_id) REFERENCES item_subtype(id),
    FOREIGN KEY (status1_id) REFERENCES status_types(id),
    FOREIGN KEY (status2_id) REFERENCES status_types(id),
    FOREIGN KEY (status3_id) REFERENCES status_types(id)
);

CREATE TABLE consumable_data(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type_id INTEGER  NOT NULL DEFAULT @joia_id,
    subtype_id INTEGER DEFAULT NULL,
    name VARCHAR(70) NOT NULL,

    FOREIGN KEY (subtype_id) REFERENCES item_subtype(id)
);

CREATE TABLE gem_data(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type_id INTEGER NOT NULL DEFAULT @material_id,
    subtype_id INTEGER NOT NULL DEFAULT @gem_id,
    name VARCHAR(40) NOT NULL,
    grade INTEGER NOT NULL,
    status1_id INTEGER NOT NULL,
    status1_val INTEGER NOT NULL,
    status2_id INTEGER DEFAULT NULL,
    status2_val INTEGER DEFAULT NULL,

    FOREIGN KEY (subtype_id) REFERENCES item_subtype(id),
    FOREIGN KEY (status1_id) REFERENCES status_types(id),
    FOREIGN KEY (status2_id) REFERENCES status_types(id)
);

CREATE TABLE planets(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL
);

INSERT INTO planets(name) VALUES('Junon');
SET @junon_id = LAST_INSERT_ID();
INSERT INTO planets(name) VALUES('Luna');
SET @luna_id = LAST_INSERT_ID();
INSERT INTO planets(name) VALUES('Eldeon');
SET @eldeon_id = LAST_INSERT_ID();
INSERT INTO planets(name) VALUES('Oro');
SET @oro_id = LAST_INSERT_ID();
INSERT INTO planets(name) VALUES('Skaaj');
SET @skaaj_id = LAST_INSERT_ID();
INSERT INTO planets(name) VALUES('Hebarn');
SET @hebarn_id = LAST_INSERT_ID();

CREATE TABLE cities(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    planet_id INTEGER NOT NULL,

    FOREIGN KEY (planet_id) REFERENCES planets(id)
);

INSERT INTO cities(name, planet_id) VALUES('City of Junon Polis', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('Adventure Plains', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('Breezy Hills', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('El Verloon Desert', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('Valley of Luxem Tower', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('Anima Lake', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('Forest of Wisdom', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('Desert of the Dead', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('Gorge of Silence', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('Goblin Cave', @junon_id);
INSERT INTO cities(name, planet_id) VALUES('Kenji Beach', @junon_id);

INSERT INTO cities(name, planet_id) VALUES('Magic City of Eucar', @luna_id);
INSERT INTO cities(name, planet_id) VALUES('Freezing Plateau', @junon_id);

CREATE TABLE quests(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    planet_id INTEGER DEFAULT NULL,
    city_id INTEGER DEFAULT NULL,

    FOREIGN KEY (planet_id) REFERENCES planets(id),
    FOREIGN KEY (city_id) REFERENCES cities(id)
);

CREATE TABLE npcs(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    planet_id INTEGER DEFAULT NULL,
    city_id INTEGER DEFAULT NULL,

    FOREIGN KEY (planet_id) REFERENCES planets(id),
    FOREIGN KEY (city_id) REFERENCES cities(id)
); 

CREATE TABLE pages(
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    page_type INTEGER NOT NULL,
    content_id INTEGER NOT NULL,
    content LONGTEXT NOT NULL,

    FOREIGN KEY (page_type) REFERENCES page_types(id) 
);






