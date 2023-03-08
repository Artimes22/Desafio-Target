export class teste3 {

}import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  dadosJson: { dia: number, valor: number }[] = [];

  constructor(private http: HttpClient) {
    this.http.get('assets/json/dados-2.json').subscribe((res) => {
      this.dadosJson = res as [{ dia: number, valor: number }];
      console.log('--- result :: ', this.dadosJson);
      this.apresentarDados();
    });
  }

  apresentarDados() {
    var apenasValores = this.dadosJson.map(dado => dado.valor);

    const menorValor = Math.min(...apenasValores);
    console.log('Menor valor', this.dadosJson.find(dado => dado.valor == menorValor));

    const maiorValor = Math.max(...apenasValores);
    console.log('Maior valor', this.dadosJson.find(dado => dado.valor == maiorValor));

    var valorTotal = 0;
    var diasContabilizados = 0;

    this.dadosJson.forEach(dado => {
      if (dado.valor > 0) {
        valorTotal += dado.valor;
        diasContabilizados += 1;
      }
    });

    var mediaMensal = valorTotal / diasContabilizados;
    console.log('media', mediaMensal);

    var diasComValorMaiorQueAMedia: number[] = [];

    this.dadosJson.forEach(dado => {
      if(dado.valor > mediaMensal){
        diasComValorMaiorQueAMedia.push(dado.dia);
      }
    });

    console.log('Dias com valor maior que a media', diasComValorMaiorQueAMedia);
    console.log('Total de dias com valor maior que a media', diasComValorMaiorQueAMedia.length);

  }

  ngOnInit() { }
}