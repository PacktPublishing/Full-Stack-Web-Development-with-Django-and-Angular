import { ComponentFixture, fakeAsync, TestBed, tick } from '@angular/core/testing'

import { ProductComponent } from './product.component'
import { ReactiveFormsModule, UntypedFormControl } from '@angular/forms'
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
import { By } from '@angular/platform-browser'
import { Product } from 'src/app/shared/model/product.model'

describe('ProductComponent', () => {
  let component: ProductComponent
  let fixture: ComponentFixture<ProductComponent>
  let nameCtrl: UntypedFormControl
  let priceCtrl: UntypedFormControl
  let currencyCtrl: UntypedFormControl

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProductComponent],
      imports: [ReactiveFormsModule],
      schemas: [CUSTOM_ELEMENTS_SCHEMA]
    });
    fixture = TestBed.createComponent(ProductComponent)
    component = fixture.componentInstance
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

  describe('Form Validation', () => {

    it('should be valid if mandatory fields are right', fakeAsync(() => {
      //spyOn(duplicatedSpotNameValidatorService, 'existingName').and.returnValue(of(null))
      fixture.whenStable().then(() => {
        expect(nameCtrl.valid).toBeTruthy()
        expect(priceCtrl.valid).toBeTruthy()
        expect(currencyCtrl.valid).toBeTruthy()
      })
      component.ngOnInit()
      givenValidInstance()
    }))

    it('should be invalid if name field is empty', fakeAsync(() => {
      //spyOn(duplicatedSpotNameValidatorService, 'existingName').and.returnValue(of(null))
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
      }))

    })

  }) 
  
})



