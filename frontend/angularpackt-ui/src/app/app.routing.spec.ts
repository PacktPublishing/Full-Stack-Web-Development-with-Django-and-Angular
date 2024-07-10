import { fakeAsync, flush, TestBed } from "@angular/core/testing";
import { Router } from "@angular/router";
import { Location } from '@angular/common';
import { RouterTestingModule } from "@angular/router/testing";
import { ProductComponent } from "./components/product/product.component";

describe('AppRouting', () => {

    let router: Router;
    let location: Location;

    beforeEach(() => {
        TestBed.configureTestingModule({
            imports: [RouterTestingModule.withRoutes([
                { path: 'product', component: ProductComponent }
            ])],
            providers: [],
            declarations: [ProductComponent],
        });
    });

    beforeEach(fakeAsync(() => {
        router = TestBed.inject(Router);
        location = TestBed.inject(Location);
        router.navigateByUrl('/');
        advance();
    }));

    function advance(): void {
        flush(); 
    }

    it('should route to the product page', fakeAsync(() => {
        router.navigateByUrl('/product');
        advance();
        expect(location.path()).toEqual('/product');
    }));

})