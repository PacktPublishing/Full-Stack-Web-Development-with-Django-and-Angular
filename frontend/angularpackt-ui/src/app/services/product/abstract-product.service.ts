import { Observable } from "rxjs"
import { Product } from "src/app/shared/model/product.model"

export abstract class AbstractProductService {

    abstract getAll(pageNumber: number): Observable<Product[]>

    abstract create(product : Product): Observable<Product>

    abstract read(id: string): Observable<Product>

    abstract update(product : Product): Observable<Product>
    
    abstract patch(product : Product): Observable<Product>

    abstract delete(id: string): Observable<any>

}
