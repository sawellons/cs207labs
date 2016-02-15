#include "bloom.h"

key_t* randarray(int n, int max) {
  key_t *arr;
  arr = (key_t*) malloc(sizeof(key_t)*n);

  for (int i=0; i<n; i++) {
    arr[i] = rand() % max;
  }
  return arr;
}

int main() {
  bloom_filter_t B;
  bloom_init(&B, 1000);

  /*  for (index_t i=1; i < 71; i++) {
    bloom_add(&B, i);
  }

  // Count number of bits set
  int count = 0;
  for (index_t j=0; j < 1000; j++) {
    //    if (get_bit(&B, j) == 1) {printf("%llu\n", j);} 
    count += get_bit(&B, j);
    } */
  //  printf("%i\n", count);

  key_t *arr1 = randarray(100, 1000000);
  key_t *arr2 = randarray(100, 1000000);
  for (int i=0; i<100; i++) {
    bloom_add(&B, arr1[i]);
  }

  int count = 0;
  for (index_t j=0; j < 1000; j++) {
    count += get_bit(&B, j);
  }
  printf("%i\n", count);

  count = 0;
  for (index_t j=0; j < 1000; j++) {
    if (bloom_check(&B, arr2[j]) == 1) {
      count++;
    }
  }
  printf("%i\n", count);


  bloom_destroy(&B);

}
