program RungeKutta2
    implicit none
    real(8) :: t, x, dt, k1, k2, t_end
    integer :: n, i

    ! ===========================
    ! First integration: 0 to 10
    ! ===========================
    t = 0.0d0
    x = 1.0d0
    dt = 0.01d0
    t_end = 10.0d0
    n = int(t_end / dt)

    open(unit=10, file="prob2-1.dat", status="replace")
    write(10,*) "t x"
    write(10,*) t, x

    do i = 1, n
        k1 = dt * (-x**3 + sin(t))
        k2 = dt * (-(x + 0.5d0*k1)**3 + sin(t + 0.5d0*dt))
        x = x + k2
        t = t + dt
        write(10,*) t, x
    end do

    close(10)

    ! ===============================
    ! Second integration: 0 to 10000
    ! ===============================
    t = 0.0d0
    x = 1.0d0
    dt = 10.0d0
    t_end = 10000.0d0
    n = int(t_end / dt)

    open(unit=11, file="prob2-2.dat", status="replace")
    write(11,*) "t x"
    write(11,*) t, x

    do i = 1, n
        k1 = dt * (-x**3 + sin(t))
        k2 = dt * (-(x + 0.5d0*k1)**3 + sin(t + 0.5d0*dt))
        x = x + k2
        t = t + dt
        write(11,*) t, x
    end do

    close(11)

    print *, "Integration complete. Results saved to prob2-1.dat and prob2-2.dat"

end program RungeKutta2
