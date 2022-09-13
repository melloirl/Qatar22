# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Selecao(models.Model):
    cod_selecao = models.IntegerField(db_column='Cod_Selecao', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    confederacao = models.CharField(db_column='Confederacao', max_length=45)  # Field name made lowercase.
    titulo = models.IntegerField(db_column='Titulo')  # Field name made lowercase.
    ranking = models.CharField(db_column='Ranking', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'selecao'

class Alojamento(models.Model):
    cod_alojamento = models.IntegerField(db_column='Cod_Alojamento', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rua = models.CharField(db_column='Rua', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    entrada = models.CharField(db_column='Entrada', max_length=45)  # Field name made lowercase.
    saida = models.CharField(db_column='Saida', max_length=45)  # Field name made lowercase.
    selecao_cod_selecao = models.ForeignKey('Selecao', models.DO_NOTHING, db_column='SELECAO_Cod_Selecao')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'alojamento'
        unique_together = (('cod_alojamento', 'selecao_cod_selecao'),)


class Arbitro(models.Model):
    cod_arbitro = models.IntegerField(db_column='Cod_Arbitro', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    idade = models.CharField(db_column='Idade', max_length=45)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=45)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=45)  # Field name made lowercase.
    confederacao = models.CharField(db_column='Confederacao', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'arbitro'


class Estadio(models.Model):
    cod_estadio = models.IntegerField(db_column='Cod_Estadio', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    capacidade = models.CharField(db_column='Capacidade', max_length=45)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=45)  # Field name made lowercase.
    ano = models.CharField(db_column='Ano', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'estadio'


class Estatistica(models.Model):
    cod_estatistica = models.IntegerField(db_column='Cod_Estatistica', primary_key=True)  # Field name made lowercase.
    golo = models.CharField(db_column='Golo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    falta = models.CharField(db_column='Falta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    amarelo = models.CharField(db_column='Amarelo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vermelho = models.CharField(db_column='Vermelho', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lesao = models.CharField(db_column='Lesao', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'estatistica'


class Grupo(models.Model):
    cod_grupo = models.IntegerField(db_column='Cod_Grupo', primary_key=True)  # Field name made lowercase.
    jogo = models.IntegerField(db_column='Jogo')  # Field name made lowercase.
    vitoria = models.IntegerField(db_column='Vitoria')  # Field name made lowercase.
    empate = models.IntegerField(db_column='Empate')  # Field name made lowercase.
    derrota = models.IntegerField(db_column='Derrota')  # Field name made lowercase.
    gm = models.IntegerField(db_column='GM')  # Field name made lowercase.
    gs = models.IntegerField(db_column='GS')  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'grupo'


class Jogador(models.Model):
    cod_jogador = models.IntegerField(db_column='Cod_Jogador', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    idade = models.IntegerField(db_column='Idade')  # Field name made lowercase.
    clubo = models.CharField(db_column='Clubo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    posicao = models.CharField(db_column='Posição', max_length=45)  # Field name made lowercase.
    titulo = models.IntegerField(db_column='Titulo')  # Field name made lowercase.
    selecao_cod_selecao = models.ForeignKey('Selecao', models.DO_NOTHING, db_column='SELECAO_Cod_Selecao')  # Field name made lowercase.
    estatistica_cod_estatistica = models.ForeignKey(Estatistica, models.DO_NOTHING, db_column='ESTATISTICA_Cod_Estatistica')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'jogador'
        unique_together = (('cod_jogador', 'selecao_cod_selecao'),)


class Marcador(models.Model):
    cod_marcador = models.IntegerField(db_column='Cod_Marcador', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    posicao = models.CharField(db_column='Posicao', max_length=45)  # Field name made lowercase.
    estatistica_cod_estatistica = models.ForeignKey(Estatistica, models.DO_NOTHING, db_column='ESTATISTICA_Cod_Estatistica')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'marcador'


class MelhorJogador(models.Model):
    cod_melhor_jogador = models.IntegerField(db_column='Cod_Melhor_Jogador', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    posicao = models.CharField(db_column='Posicao', max_length=45)  # Field name made lowercase.
    estatistica_cod_estatistica = models.ForeignKey(Estatistica, models.DO_NOTHING, db_column='ESTATISTICA_Cod_Estatistica')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'melhor_jogador'


class Partida(models.Model):
    cod_partida = models.IntegerField(db_column='Cod_Partida', primary_key=True)  # Field name made lowercase.
    inicio = models.TimeField(db_column='Inicio', blank=True, null=True)  # Field name made lowercase.
    final = models.TimeField(db_column='Final', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    golo_casa = models.IntegerField(db_column='Golo_Casa', blank=True, null=True)  # Field name made lowercase.
    marcodor = models.CharField(db_column='Marcodor', max_length=45, blank=True, null=True)  # Field name made lowercase.
    golo_visitante = models.IntegerField(db_column='Golo_Visitante', blank=True, null=True)  # Field name made lowercase.
    selecao_cod_selecao = models.ForeignKey('Selecao', on_delete=models.CASCADE,related_name = 'time_casa')  # Field name made lowercase.
    selecao_cod_selecao1 = models.ForeignKey('Selecao', on_delete=models.CASCADE,related_name = 'time_fora')  # Field name made lowercase.
    estadio_cod_estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, db_column='ESTADIO_Cod_Estadio')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'partida'
        unique_together = (('cod_partida', 'selecao_cod_selecao', 'selecao_cod_selecao1', 'estadio_cod_estadio'),)


class PartidaHasArbitro(models.Model):
    partida_cod_partida = models.OneToOneField(Partida, models.DO_NOTHING, db_column='PARTIDA_Cod_Partida', primary_key=True)  # Field name made lowercase.
    partida_selecao_cod_selecao = models.ForeignKey(Partida, on_delete=models.CASCADE,related_name ='time_casa')  # Field name made lowercase.
    partida_selecao_cod_selecao1 = models.ForeignKey(Partida,on_delete=models.CASCADE,related_name ='time_fora')  # Field name made lowercase.
    partida_estadio_cod_estadio = models.ForeignKey(Partida, on_delete=models.CASCADE, db_column='PARTIDA_ESTADIO_Cod_Estadio', to_field='ESTADIO_Cod_Estadio')  # Field name made lowercase.
    arbitro_cod_arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE, db_column='ARBITRO_Cod_Arbitro')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'partida_has_arbitro'
        unique_together = (('partida_cod_partida', 'partida_selecao_cod_selecao', 'partida_selecao_cod_selecao1', 'partida_estadio_cod_estadio', 'arbitro_cod_arbitro'),)


# class PartidaHasEstatistica(models.Model):
#     partida_cod_partida = models.OneToOneField(Partida, models.DO_NOTHING, db_column='PARTIDA_Cod_Partida', primary_key=True)  # Field name made lowercase.
#     partida_selecao_cod_selecao = models.ForeignKey(Partida, models.DO_NOTHING, db_column='PARTIDA_SELECAO_Cod_Selecao', to_field='SELECAO_Cod_Selecao')  # Field name made lowercase.
#     partida_selecao_cod_selecao1 = models.ForeignKey(Partida, models.DO_NOTHING, db_column='PARTIDA_SELECAO_Cod_Selecao1', to_field='SELECAO_Cod_Selecao1')  # Field name made lowercase.
#     partida_estadio_cod_estadio = models.ForeignKey(Partida, models.DO_NOTHING, db_column='PARTIDA_ESTADIO_Cod_Estadio', to_field='ESTADIO_Cod_Estadio')  # Field name made lowercase.
#     estatistica_cod_estatistica = models.ForeignKey(Estatistica, models.DO_NOTHING, db_column='ESTATISTICA_Cod_Estatistica')  # Field name made lowercase.

#     class Meta:
#         managed = True
#         db_table = 'partida_has_estatistica'
#         unique_together = (('partida_cod_partida', 'partida_selecao_cod_selecao', 'partida_selecao_cod_selecao1', 'partida_estadio_cod_estadio', 'estatistica_cod_estatistica'),)


# class SelecaoHasGrupo(models.Model):
#     selecao_cod_selecao = models.OneToOneField(Selecao, models.DO_NOTHING, db_column='SELECAO_Cod_Selecao', primary_key=True)  # Field name made lowercase.
#     grupo_cod_grupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='GRUPO_Cod_Grupo')  # Field name made lowercase.

#     class Meta:
#         managed = True
#         db_table = 'selecao_has_grupo'
#         unique_together = (('selecao_cod_selecao', 'grupo_cod_grupo'),)


class Treinador(models.Model):
    cod_treinador = models.IntegerField(db_column='Cod_Treinador', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    idade = models.IntegerField(db_column='Idade')  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=45)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=45)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    selecao_cod_selecao = models.ForeignKey(Selecao, models.DO_NOTHING, db_column='SELECAO_Cod_Selecao')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'treinador'
        unique_together = (('cod_treinador', 'selecao_cod_selecao'),)
