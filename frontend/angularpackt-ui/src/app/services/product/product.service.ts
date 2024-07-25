import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core'
import { Observable } from 'rxjs'
import { AbstractProductService } from './abstract-product.service'
import { Product } from 'src/app/shared/model/product.model'


@Injectable({
  providedIn: 'root'
})
export class ProductService extends AbstractProductService {

  products$!: Observable<Product[]> 
  products: Product[] = []
  apiURL

  constructor(private _httpClient: HttpClient) {
    super()
    this.apiURL = 'http://localhost:8000/api/v0/products/'
  }

  override getAll(pageNumber: number): Observable<Product[]> {
    return this._httpClient.get<Product[]>(this.apiURL + '?page=' + pageNumber)
  }

  override create(product: Product): Observable<Product> {
    return this._httpClient.post<Product>(this.apiURL, product)
  }

  override read(id: string): Observable<Product> {
    return this._httpClient.get<Product>(this.apiURL + id)
  }

  override update(product: Product): Observable<Product> {
    return this._httpClient.put<Product>(this.apiURL + product.id, product)
  }

  override patch(product: Product): Observable<Product> {
    return this._httpClient.patch<Product>(this.apiURL + product.id, product)
  }

  override delete(id: string): Observable<any> {
    return this._httpClient.delete<Product>(this.apiURL + id)
  }

}
