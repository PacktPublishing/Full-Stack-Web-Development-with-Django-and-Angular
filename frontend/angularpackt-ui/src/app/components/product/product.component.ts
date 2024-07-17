import { Component, OnInit, ViewChild } from '@angular/core';
import { UntypedFormGroup, UntypedFormBuilder, Validators, UntypedFormControl } from '@angular/forms'
import { Router } from '@angular/router';
import { Currencies, Currency } from 'src/app/shared/convert/currency';
import { Product } from 'src/app/shared/model/product.model';

@Component({
  selector: 'apui-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  productForm!: UntypedFormGroup;
  nameCtrl!: UntypedFormControl
  priceCtrl!: UntypedFormControl
  currencyCtrl!: UntypedFormControl
  product!: Product;
  mainCurrencies: Currency[] = Currencies.mainCurrencies
  @ViewChild('nameError') nameErrorMessage: any
  @ViewChild('priceError') priceErrorMessage: any
  @ViewChild('currencyError') currencyErrorMessage: any

  constructor(private _router: Router,
    private _formBuilder: UntypedFormBuilder
    ) { }

  ngOnInit(): void {
    this.productForm = this._formBuilder.group({
      name: [{ value: 'Change name here!', disabled: false },
        {
          validators: [Validators.required, Validators.minLength(4), Validators.maxLength(50)],
          updateOn: "blur"
        }
      ],
      price: [{ value: '1', disabled: false },
        {
          validators: [Validators.required],
          updateOn: "blur"
        }
      ],
      currency: [{ value: '€', disabled: false },
        {
          validators: [Validators.required],
          updateOn: "blur"
        }
      ],
    })
    this.nameCtrl = this.productForm.get('name') as UntypedFormControl
    this.priceCtrl = this.productForm.get('price') as UntypedFormControl
    this.currencyCtrl = this.productForm.get('currency') as UntypedFormControl
  }

  selectionChanged ($event: any) {
    switch ($event.value) {
      case '€': {
        this.currencyCtrl.setValue('EUR')
        break
      }
      case '$': {
        this.currencyCtrl.setValue('USD')
        break
      }
      default: {
        this.currencyCtrl.setValue($event.value)
        break
      }
    }
    console.log('currency valueChange', $event)
  }

  getInvalidNameErrorMessage () {
    return this.nameCtrl.hasError('required') ? 'Name is required' :
      this.nameCtrl.hasError('minlength') ? 'Name is too short' :
        this.nameCtrl.hasError('maxlength') ? 'Name is too long' : ''
  }

  getInvalidPriceErrorMessage () {
    return this.priceCtrl.hasError('required') ? 'Price is required' : '' 
  }

  getInvalidCurrencyErrorMessage () {
    return this.currencyCtrl.hasError('required') ? 'Currency is required, EUR (€) or USD ($)' : '' 
  }

  formIsReady (): boolean {
    return this.productForm.valid && this.productForm.dirty
  }

  onSubmit () {
    if (this.formIsReady()) {
      let name = this.productForm.value.name
      let price = this.productForm.value.price
      let currency = this.productForm.value.currency
      if (this.productForm.dirty) {
        this.product = new Product(name, price, currency)
      } 
      //this._router.navigateByUrl('/product-search')
    }
    console.log('Creating new Product: ', this.product)
  }


}
