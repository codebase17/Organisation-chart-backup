import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OrganisationMainComponent } from './organisation-main.component';

describe('OrganisationMainComponent', () => {
  let component: OrganisationMainComponent;
  let fixture: ComponentFixture<OrganisationMainComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OrganisationMainComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OrganisationMainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
