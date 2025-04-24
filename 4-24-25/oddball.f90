
program oddball_integration
  implicit none
  
  integer, parameter :: dp = kind(1.0d0)
  integer :: i, count, N
  real(dp) :: x, y, b, r, theta
  real(dp) :: Z, e, bigE, epsilon0, a0, sigma, reflect_limit
  real(dp) :: u1, u2


  ! Same constants as Python
  Z = 79.0
  e = 1.602d-19
  bigE = 7.7d6 * e
  epsilon0 = 8.854d-12
  a0 = 5.292d-11
  sigma = a0 / 100.0
  
  N = 1d9 

  ! Init count to be 0
  count = 0

  ! Make random seed
  call random_seed()  

  ! Same equation as Python, but manual Pi value and float stuff
  reflect_limit = Z * e**2 / (2.0 * 3.141592653589793 * epsilon0 * bigE)

  ! for loop for plugging into equation as well as calculating the gaussian inside instead of seperate function
  do i = 1, N
     call random_number(u1)
     call random_number(u2)
     
     r = sqrt(-2.0 * sigma**2 * log(1.0 - u1))
     theta = 2.0 * 3.141592653589793 * u2
     x = r * cos(theta)
     y = r * sin(theta)
     b = sqrt(x**2 + y**2)

     if (b < reflect_limit) then
        count = count + 1
     end if
  end do

  ! Print results
  print *, count, "particles were reflected out of", N

end program oddball_integration