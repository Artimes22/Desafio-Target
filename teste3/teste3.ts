import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  dadosJson: { dia: number, valor: number }[] = [];
  public menorValor = 0;
  public menorValorSemFeriadosEFinaisDeSemana = 0;
  public DiaComMenorValorSemFeriadosEFinaisDeSemana = 0;
  public diaComMenorValor = 0;

  public maiorValor = 0;
  public diaComMaiorValor = 0;

  public mediaMensal = 0;
  public diasComValorMaiorQueAMedia: number[] = [];
  public TotalDeDiasComValorMaiorQueAMedia = 0;

  constructor(private http: HttpClient) {
    this.http.get('assets/json/dados01.json').subscribe((res) => {
      this.dadosJson = res as [{ dia: number, valor: number }];
      console.log('--- result :: ', this.dadosJson);
      this.apresentarDados();
    });
  }

  public apresentarDados() {
    let apenasValores = this.dadosJson.map(dado => dado.valor);

    this.menorValor = Math.min(...apenasValores);
    this.diaComMenorValor = this.dadosJson.filter(dado => dado.valor == this.menorValor)[0].dia;

    this.menorValorSemFeriadosEFinaisDeSemana = Math.min(...apenasValores.filter(dados => dados > 0));
    this.DiaComMenorValorSemFeriadosEFinaisDeSemana = this.dadosJson.filter(dado => dado.valor == this.menorValorSemFeriadosEFinaisDeSemana)[0].dia;


    this.maiorValor = Math.max(...apenasValores);
    this.diaComMaiorValor = this.dadosJson.filter(dado => dado.valor == this.maiorValor)[0].dia;

    let valorTotal = 0;
    let diasContabilizados = 0;

    this.dadosJson.forEach(dado => {
      if (dado.valor > 0) {
        valorTotal += dado.valor;
        diasContabilizados += 1;
      }
    });

    this.mediaMensal = valorTotal / diasContabilizados;
    console.log('media', this.mediaMensal);

    this.dadosJson.forEach(dado => {
      if (dado.valor > this.mediaMensal) {
        this.diasComValorMaiorQueAMedia.push(dado.dia);
      }
    });

    this.TotalDeDiasComValorMaiorQueAMedia = this.diasComValorMaiorQueAMedia.length;

    console.log('Dias com valor maior que a media', this.diasComValorMaiorQueAMedia);
    console.log('Total de dias com valor maior que a media', this.TotalDeDiasComValorMaiorQueAMedia);
  }
}
