import { HttpClient, HttpErrorResponse } from '@angular/common/http'
import { Injectable } from '@angular/core'
import { filter, Observable, of, tap } from 'rxjs'
import { AbstractProductService } from './abstract-product.service'
import { Product } from 'src/app/shared/model/product.model'

@Injectable({
  providedIn: 'root'
})
export class MockProductService extends AbstractProductService {

  products$: Observable<Product[]> 
  products: Product[] = []
  
  constructor(private _httpClient: HttpClient) {
    super()
    const fakeURL: string = 'assets/products.json'
    this.products$ = this._httpClient.get<Product[]>(fakeURL)
  }

  override getAll(pageNumber: number): Observable<Product[]> {
    const pageSize = 5
    const initialRecord = pageNumber * pageSize - pageSize
    console.log('All Products Found: ' + this.products$ + ' and showing page:' + pageNumber)
    return this.products$
  }

  override create(product : Product): Observable<Product> {
    console.log('New Product Created: ' + product)
    return of(product)
  }

  override read(id: string): Observable<Product> {
    let product: Product = this.findProductById(id)
    console.log('Product Found: ' + product)
    return of(product)
  }

  override update(product: Product): Observable<Product> {
    product = this.findProductById(product.id)
    console.log('Product Updated: ' + product)
    return of(product)
  }

  override patch(product: Product): Observable<Product> {
    product = this.findProductById(product.id)
    console.log('Product partially Updated: ' + product)
    return of(product)
  }

  override delete(id: string): Observable<any> {
    let product = this.findProductById(id)
    console.log('Product Deleted: ' + product)
    return of(true)
  }

  private findProductById(id: string): Product {
    this.products$.subscribe(data => {
      this.products = data,
      (err: HttpErrorResponse) => console.log(`Error retrieving Products from file: ${err}`)
    })
    return this.products.filter((product) => product.id == id)[0]
  }

}

