
describe('login', () => {
  it("Container and text-area in login", () => {
    cy.visit('http://127.0.0.1:8000/login/')
    cy.get("h4").contains("Bienvenido a Zinfonia")
    cy.get('label').should('contain', 'Usuario').and('contain', 'Contraseña')
  })
  it("input accessible", () => {
    cy.visit('http://127.0.0.1:8000/login/')
    cy.get('.block')
    cy.get('input[type=text]').get('input[type=password]')
    cy.get('#id_username').type('user040603')
    cy.get('#id_password')
    cy.get('form')
    cy.get('input[type=submit]').click().get('input[type=reset]').click()

  })
  it('disables on click', () => {
    cy.visit('http://127.0.0.1:8000/login/')
    cy.get('a[href]').click()
  })})
describe('sign in', () => {
  it("Container and text-area in sign", () => {
      cy.visit('http://127.0.0.1:8000/sing/')
      cy.get("h4").contains("Registrate")
      cy.get('label').should('contain', 'Nombres').and('contain', 'Apellidos')
      .and('contain', 'Usuario').and('contain', 'Contraseña').and('contain', 'Confirmar Contraseña')
  })
  it("form accessible", () => {
      cy.get('form')
      cy.get('.form-control')
      cy.get('input[type=text]').get('input[type=password]')
      cy.get('.btn.btn-primary')
  })
  it('disables on click', () => {
      cy.get('a[href]').click()
  })})
describe('logout', () => {
  it("Container and text-area in logout", () => {
      cy.visit('http://127.0.0.1:8000/logout/')
      cy.get("h2").contains("Sesión cerrada")
      cy.get("p").contains("Haz cerrado sesión correctamente. Que tengas un excelente día!!") 
      cy.get("p").contains('Si te falto algo, inicia sesión nuevamente')
      cy.get('a[href]').click()
  })})
describe('inventarios', () => {
    it("Can make a crud in inventarios with method POST", () => {
        cy.visit('http://127.0.0.1:8000/paginas')
        cy.get('.header')
        cy.get('a[href]')
        cy.get('h1').contains('Zinfonia market')
        cy.get('label')
      })  
    it("check table and their components", () => {    
        cy.get('table').should('have.class', 'table table-sm table-bordered')
        cy.get('tbody').should('have.class', 'tbody-lg')
        cy.get('th')
        cy.get('td')
        cy.get('a').should('have.class', 'btn btn-success btn-block btn-sm').and('have.attr', 'href')
        cy.get('a').should('have.class', 'btn btn-danger btn-block btn-sm').and('have.attr', 'href')
    })})
describe('Agregar', () => {
    it("form add products with method POST", () => {
        cy.visit('http://127.0.0.1:8000/agregar')
        cy.get('.header')
        cy.get('a[href]')
        cy.get('h1').contains('Zinfonia market')
        cy.get('label')  })
    it("check form", () => {    
        cy.get('form')
        cy.get('label').should('contain', 'Producto')
        .and('contain', 'Tipo').and('contain', 'Valor entrada')
        .and('contain', 'Valor venta').and('contain', 'Distribuidor')
        .and('contain', 'Marca').and('contain', 'Factura')
        .and('contain', 'Fecha de vencimiento')
  })
})
describe('Editar', () => {
  it("form edit products with method POST", () => {
      cy.visit('http://127.0.0.1:8000/editar/14')
      cy.get('.header')
      cy.get('a[href]')
      cy.get('h1').contains('Zinfonia market')
      cy.get('label')  })
  it("check form", () => {    
      cy.get('form')
      cy.get('label').should('contain', 'Producto')
      .and('contain', 'Tipo').and('contain', 'Valor entrada')
      .and('contain', 'Valor venta').and('contain', 'Distribuidor')
      .and('contain', 'Marca').and('contain', 'Factura')
      .and('contain', 'Fecha de vencimiento')
})
})
describe('Marca', () => {
  it("insert marca", () => {
      cy.visit('http://127.0.0.1:8000/Qmarca/')
      cy.get('.header')
      cy.get('a[href]')
      cy.get('h4').contains('Marca')
      cy.get('label')  })
  it("check form and table", () => {    
    cy.get('form')
    cy.get('label').should('contain', 'Marca')
    cy.get('tbody').should('have.class', 'tbody-lg')
    cy.get('th')
    cy.get('td')
})
})
describe('Distribuidor', () => {
  it("insert distribuidor", () => {
      cy.visit('http://127.0.0.1:8000/Distribuidores/')
      cy.get('.header')
      cy.get('a[href]')
      cy.get('h4').contains('Distribuidores')
      cy.get('label')  })
  it("check form and table", () => {    
    cy.get('form')
    cy.get('label').should('contain', 'Distribuidores')
    cy.get('tbody').should('have.class', 'tbody-lg')
    cy.get('th')
    cy.get('td')
})
})
describe('Tipo', () => {
  it("insert tipo", () => {
      cy.visit('http://127.0.0.1:8000/Qtipo/')
      cy.get('.header')
      cy.get('a[href]')
      cy.get('h4').contains('Tipo')
      cy.get('label')  })
  it("check form and table", () => {    
    cy.get('form')
    cy.get('label').should('contain', 'Tipo')
    cy.get('tbody').should('have.class', 'tbody-lg')
    cy.get('th')
    cy.get('td')
})
})
    



  
    


