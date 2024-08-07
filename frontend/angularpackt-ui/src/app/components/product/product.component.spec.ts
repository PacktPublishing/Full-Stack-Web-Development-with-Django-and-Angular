import { ComponentFixture, fakeAsync, TestBed, tick, waitForAsync } from '@angular/core/testing'
import { ReactiveFormsModule, UntypedFormControl } from '@angular/forms'
import { HttpClientModule } from '@angular/common/http'
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { MatSelect } from '@angular/material/select'
import { By } from '@angular/platform-browser'
import { of } from 'rxjs'
import { Product } from 'src/app/shared/model/product.model'
import { ProductComponent } from './product.component'
import { AbstractProductService } from 'src/app/services/product/abstract-product.service'

describe('ProductComponent', () => {
  let component: ProductComponent
  let fixture: ComponentFixture<ProductComponent>
  let nameCtrl: UntypedFormControl
  let priceCtrl: UntypedFormControl
  let currencyCtrl: UntypedFormControl
  let productService: AbstractProductService

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProductComponent],
      imports: [ReactiveFormsModule, HttpClientModule],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
      providers: [AbstractProductService]
    });
    fixture = TestBed.createComponent(ProductComponent)
    component = fixture.componentInstance
    productService = fixture.debugElement.injector.get(AbstractProductService)
    spyOn(productService, 'getAll').and.returnValue(of([]))
    fixture.detectChanges()
  });

  it('should create the Component Form', () => {
    expect(component).toBeTruthy()
    const rootElement = fixture.debugElement
    expect(rootElement.query(By.css('[data-testid=name]'))).toBeTruthy()
    expect(rootElement.query(By.css('[data-testid=price]'))).toBeTruthy()
    expect(rootElement.query(By.css('[data-testid=currency]'))).toBeTruthy()
  });

  function givenValidInstance (): void {
    nameCtrl = component.nameCtrl
    priceCtrl = component.priceCtrl
    currencyCtrl = component.currencyCtrl
   
    nameCtrl.setValue('PRODUCT NAME')
    priceCtrl.setValue('54')
    currencyCtrl.setValue('EUR')
  }

  describe('Form operation', () => {

    it(`should log the value when currency is selected`, waitForAsync(() => {
        const consoleSpy = spyOn(console, 'log')
        const $selectChangeEvent = { source: MatSelect, value: 'USD' }
        fixture.whenStable().then(() => {
          expect(component.currencyCtrl.value).toEqual('USD')
          expect(component.currencyCtrl.valid).toBeTruthy()
          expect(consoleSpy).toHaveBeenCalledWith('currency valueChange', $selectChangeEvent)
        })
        component.selectionChanged($selectChangeEvent)
      })
    )

  })

  describe('Form Validation', () => {

    it('should be valid if mandatory fields are right', fakeAsync(() => {
      fixture.whenStable().then(() => {
        expect(nameCtrl.valid).toBeTruthy()
        expect(priceCtrl.valid).toBeTruthy()
        expect(currencyCtrl.valid).toBeTruthy()
      })
      component.ngOnInit()
      givenValidInstance()
    }))

    it('should be invalid if name field is empty', fakeAsync(() => {
      fixture.whenStable().then(() => {
        givenValidInstance()
        nameCtrl.setValue("")
        fixture.detectChanges()
        expect(nameCtrl.valid).toBeFalsy()
        let errors = nameCtrl.errors || {}
        expect(errors['required']).toBeTruthy()
        expect(component.nameErrorMessage.nativeElement.textContent).toContain(' Name is required ! ')
        expect(component.productForm.valid).toBeFalsy()
      })
      component.ngOnInit()
    }))

    it('should be invalid if name field is too short', fakeAsync(() => {
      fixture.whenStable().then(() => {
        givenValidInstance()
        nameCtrl.setValue("123")
        fixture.detectChanges()
        expect(nameCtrl.valid).toBeFalsy()
        let errors = nameCtrl.errors || {}
        expect(errors['minlength']).toBeTruthy()
        expect(errors['maxlength']).toBeFalsy()
        expect(component.nameErrorMessage.nativeElement.textContent).toContain(' Name is too short ! ')
        expect(component.productForm.valid).toBeFalsy()
      })
      component.ngOnInit()
    }))

    it('should be invalid if name field is too long', fakeAsync(() => {
      fixture.whenStable().then(() => {
        givenValidInstance()
        nameCtrl.setValue("123456789012345678901234567890123456789012345678901")
        fixture.detectChanges()
        expect(nameCtrl.valid).toBeFalsy()
        let errors = nameCtrl.errors || {}
        expect(errors['minlength']).toBeFalsy()
        expect(errors['maxlength']).toBeTruthy()
        expect(component.nameErrorMessage.nativeElement.textContent).toContain(' Name is too long ! ')
        expect(component.productForm.valid).toBeFalsy()
      })
      component.ngOnInit()
    }))

    it('should be invalid if price field is empty', fakeAsync(() => {
      fixture.whenStable().then(() => {
        givenValidInstance()
        priceCtrl.setValue("")
        fixture.detectChanges()
        expect(priceCtrl.valid).toBeFalsy()
        let errors = priceCtrl.errors || {}
        expect(errors['required']).toBeTruthy()
        expect(component.priceErrorMessage.nativeElement.textContent).toContain(' Price is required ! ')
        expect(component.productForm.valid).toBeFalsy()
      })
      component.ngOnInit()
    }))

    it('should be invalid if currency field is empty', fakeAsync(() => {
      fixture.whenStable().then(() => {
        givenValidInstance()
        currencyCtrl.setValue("")
        fixture.detectChanges()
        expect(currencyCtrl.valid).toBeFalsy()
        let errors = currencyCtrl.errors || {}
        expect(errors['required']).toBeTruthy()
        expect(component.currencyErrorMessage.nativeElement.textContent).toContain(' Currency is required, EUR (€) or USD ($) ! ')
        expect(component.productForm.valid).toBeFalsy()
      })
      component.ngOnInit()
    }))

  })

  describe('Form Submit', () => {

    describe('Product Creation', () => {

      it('should submit the form for creation', fakeAsync(() => {
        const expectedProduct = new Product(component.productForm.value.name,
          component.productForm.value.price,
          component.productForm.value.currency)
        const createProductServiceSpy = spyOn(productService, 'create').and.returnValue(of(expectedProduct))    
        fixture.whenStable().then(() => {
          expect(component.productForm.valid).toBeTruthy()
          expect(component.productForm.dirty).toBeTruthy()
          tick(300)
          fixture.detectChanges()
          //expect(location.path()).toEqual('/spot-search')
        })
        component.ngOnInit()
        givenValidInstance()
        component.productForm.markAsDirty()
        component.onSubmit()
        expect(createProductServiceSpy).toHaveBeenCalledTimes(1)
      }))

    })

  }) 
  
})



