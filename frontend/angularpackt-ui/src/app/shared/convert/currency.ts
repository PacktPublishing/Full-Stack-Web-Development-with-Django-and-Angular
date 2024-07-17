export interface Currency {
    value: string
    viewValue: string 
  }  

export class Currencies {
  static mainCurrencies: Currency[] = [
    { value: '€', viewValue: 'Euro (€)' },
    { value: '$', viewValue: 'Dollar ($)' },
  ]
  static otherCurrencies: Currency[] = [
    { value: 'Pound', viewValue: 'Pound' },
    { value: 'Yen', viewValue: 'Yen' }
  ]
}  