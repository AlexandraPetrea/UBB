#pragma once
#include "Film.h"

//typedef Film TElement;
template <typename T>
class DynamicVector
{
private:
	T * elems;
	int size;
	int capacity;

public:
	// default constructor for a DynamicVector
	DynamicVector(int capacity = 10);

	// copy constructor for a DynamicVector
	DynamicVector(const DynamicVector& v);
	~DynamicVector();

	// assignment operator for a DynamicVector
	DynamicVector& operator=(const DynamicVector& v);
	friend DynamicVector& operator+(DynamicVector& v, const T& e);
	friend DynamicVector& operator+(const T& e, DynamicVector &v);

	// Adds an element to the current DynamicVector.
	void add(const T& e);
	void Delete(int pos);
	void update(int pos, const T& t);
	T& operator[](int pos);

	int getSize() const;
	T* getAllElems() const;

private:
	// Resizes the current DynamicVector, multiplying its capacity by a given factor (real number).
	void resize(double factor = 2);
};
template <typename T>
DynamicVector<T>::DynamicVector(int capacity)
{
	this->size = 0;
	this->capacity = capacity;
	this->elems = new T[capacity];
}
template <typename T>
DynamicVector<T>::DynamicVector(const DynamicVector<T>& v)
{
	this->size = v.size;
	this->capacity = v.capacity;
	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];
}
template <typename T>
DynamicVector<T>::~DynamicVector()
{
	delete[] this->elems;
}
template <typename T>
DynamicVector<T>& operator+ (DynamicVector<T>& v, const T& e)
{
	if (v.size == v.capacity)
		v.resize();
	v.elems[v.size] = e;
	v.size++;
	return v;
}
template <typename T>
DynamicVector<T>& operator+ (const T& e, DynamicVector<T>& v)
{
	if (v.size == v.capacity)
		v.resize();
	v.elems[v.size] = e;
	v.size++;
	return v;
}

template <typename T>
T& DynamicVector<T>::operator[](int pos)
{
	return this->elems[pos];
}

template <typename T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector<T>& v)
{
	if (this == &v)
		return *this;

	this->size = v.size;
	this->capacity = v.capacity;

	delete[] this->elems;
	this->elems = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];

	return *this;
}
template <typename T>
void DynamicVector<T>::add(const T& e)
{
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size] = e;
	this->size++;
}
template <typename T>
void DynamicVector<T>::Delete(int pos)
{
	int i, l = this->size - 1;
	for (i = pos; i < l; i++)
		this->elems[i] = this->elems[i + 1];
	this->size--;
}
template <typename T>
void DynamicVector<T>::update(int pos, const T& t)
{
	this->elems[pos] = t;
}
template <typename T>
void DynamicVector<T>::resize(double factor)
{
	this->capacity *= static_cast<int>(factor);

	T* els = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		els[i] = this->elems[i];

	delete[] this->elems;
	this->elems = els;
}
template <typename T>
T* DynamicVector<T>::getAllElems() const
{
	return this->elems;
}
template <typename T>
int DynamicVector<T>::getSize() const
{
	return this->size;
}

