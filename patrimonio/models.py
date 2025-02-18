from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

class Bem(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    numero_serie = models.CharField(max_length=100, unique=True)
    codigo_rfid = models.CharField(max_length=50, unique=True)  # Campo para simular RFID
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    data_aquisicao = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.codigo_rfid}"

class Movimentacao(models.Model):
    bem = models.ForeignKey(Bem, on_delete=models.CASCADE)
    origem = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="origem")
    destino = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="destino")
    data_movimentacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bem.nome} movido de {self.origem} para {self.destino}"
