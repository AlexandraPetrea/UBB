#include "DynamicVector.h"

/*
DynamicVector::DynamicVector(int capacity)
{
	this->size = 0;
	this->capacity = capacity;
	this->elems = new TElement[capacity];
}

DynamicVector::DynamicVector(const DynamicVector& v)
{
	this->size = v.size;
	this->capacity = v.capacity;
	this->elems = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];
}

DynamicVector::~DynamicVector()
{
	delete[] this->elems;
}

DynamicVector& operator+ (DynamicVector& v, const TElement& e)
{
	if (v.size == v.capacity)
		v.resize();
	v.elems[v.size] = e;
	v.size++;
	return v;
}
DynamicVector& operator+ (const TElement& e, DynamicVector& v)
{
	if (v.size == v.capacity)
		v.resize();
	v.elems[v.size] = e;
	v.size++;
	return v;
}

DynamicVector& DynamicVector::operator=(const DynamicVector& v)
{
	if (this == &v)
		return *this;

	this->size = v.size;
	this->capacity = v.capacity;

	delete[] this->elems;
	this->elems = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];

	return *this;
}

void DynamicVector::add(const TElement& e)
{
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size] = e;
	this->size++;
}

void DynamicVector::Delete(int pos)
{
	int i, l = this->size - 1;
	for (i = pos; i < l; i++)
		this->elems[i] = this->elems[i + 1];
	this->size--;
}

void DynamicVector::update(int pos, const TElement& t)
{
	this->elems[pos] = t;
}

void DynamicVector::resize(double factor)
{
	this->capacity *= static_cast<int>(factor);

	TElement* els = new TElement[this->capacity];
	for (int i = 0; i < this->size; i++)
		els[i] = this->elems[i];

	delete[] this->elems;
	this->elems = els;
}

TElement* DynamicVector::getAllElems() const
{
	return this->elems;
}

int DynamicVector::getSize() const
{
	return this->size;
}
*/