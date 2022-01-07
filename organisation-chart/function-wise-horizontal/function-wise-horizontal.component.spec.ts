import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FunctionWiseHorizontalComponent } from './function-wise-horizontal.component';

describe('FunctionWiseHorizontalComponent', () => {
  let component: FunctionWiseHorizontalComponent;
  let fixture: ComponentFixture<FunctionWiseHorizontalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FunctionWiseHorizontalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FunctionWiseHorizontalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
