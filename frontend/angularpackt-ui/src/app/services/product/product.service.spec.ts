import { TestBed } from '@angular/core/testing'
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing'
import { ProductService } from './product.service'
import { Product } from 'src/app/shared/model/product.model'

describe('ProductService', () => {

  let service: ProductService;
  let httpTestingController: HttpTestingController

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ ProductService ]
    })
    service = TestBed.inject(ProductService)
    httpTestingController = TestBed.inject(HttpTestingController)
    setupInstance()
  })

  it('Service should be created', () => {
    expect(service).toBeTruthy();
  })

  const instanceId = '1'
  let instance: Product

  function setupInstance () {
    instance = new Product('PRODUCT NAME', 23, 'EUR')
  }

  describe('Get All', () => {

    const instances = [
      { id: '1', name: 'PRODUCT NAME 1', price: 23, currency: 'EUR' },
      { id: '2', name: 'PRODUCT NAME 2', price: 43, currency: 'USD' },
      { id: '3', name: 'PRODUCT NAME 3', price: 44, currency: 'USD' },
      { id: '4', name: 'PRODUCT NAME 4', price: 76, currency: 'EUR' },
      { id: '5', name: 'PRODUCT NAME 5', price: 54, currency: 'EUR' }]

    it('should find all Instances with pagination', () => {
      service.getAll(1).subscribe(instances => {
        expect(instances.length).toBe(5)
        expect(instances[0].name).toEqual('PRODUCT NAME 1')
        expect(instances[1].name).toEqual('PRODUCT NAME 2')
        expect(instances[2].name).toEqual('PRODUCT NAME 3')
        expect(instances[3].name).toEqual('PRODUCT NAME 4')
        expect(instances[4].name).toEqual('PRODUCT NAME 5')
      })
      const request = httpTestingController.expectOne({ url: 'http://localhost:8000/api/v0/products/?page=1', method: 'GET' })
      request.flush(instances)
    })

  })

  describe('Create', () => {

    it('should create an Instance', () => {
      service.create(instance).subscribe(instance => {
        expect(instance.name).toEqual('PRODUCT NAME')
      })
      const request = httpTestingController.expectOne({ url: 'http://localhost:8000/api/v0/products/', method: 'POST' })
      request.flush(instance)
    })

  })

  describe('Read', () => {

    it('should read an Instance', () => {
      service.read(instanceId).subscribe(instance => {
        expect(instance.name).toEqual('PRODUCT NAME')
      })
      const request = httpTestingController.expectOne({ url: `http://localhost:8000/api/v0/products/${instanceId}`, method: 'GET' })
      request.flush(instance)
    })

  })

  describe('Update', () => {

    it('should update an Instance', () => {
      instance.id = instanceId
      service.update(instance).subscribe(instance => {
        expect(instance.name).toEqual('PRODUCT NAME')
      })
      const request = httpTestingController.expectOne({ url: `http://localhost:8000/api/v0/products/${instanceId}`, method: 'PUT' })
      request.flush(instance)
    })

  })

  describe('Partial Update', () => {

    it('should partially update an Instance', () => {
      instance.id = instanceId
      service.patch(instance).subscribe(instance => {
        expect(instance.name).toEqual('PRODUCT NAME')
      })
      const request = httpTestingController.expectOne({ url: `http://localhost:8000/api/v0/products/${instanceId}`, method: 'PATCH' })
      request.flush(instance)
    })

  })

  describe('Delete', () => {

    it('should delete an Instance', () => {
      service.delete(instanceId).subscribe(instance => {
        expect(instance.name).toEqual('PRODUCT NAME')
      })
      const request = httpTestingController.expectOne({ url: `http://localhost:8000/api/v0/products/${instanceId}`, method: 'DELETE' })
      request.flush(instance)
    })

  })

})
