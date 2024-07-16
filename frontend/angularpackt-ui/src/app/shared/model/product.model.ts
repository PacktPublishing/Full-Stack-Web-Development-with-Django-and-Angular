export class Product {
    id!: string
    name: string
    price: number
    currency: string

    /* Only one constructor is possible */
    constructor(
        name: string,
        price: number,
        currency: string) {
        this.name = name
        this.price = price
        this.currency = currency
        console.log("Product[name: " + name + ", price: " + price + ", curency: " + currency + "]")
    }
}