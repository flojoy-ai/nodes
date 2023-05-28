from flojoy import DataContainer, flojoy
import numpy.linalg

@flojoy
def EIGH(dc, params):
	'''
		
		Return the eigenvalues and eigenvectors of a complex Hermitian
		(conjugate symmetric) or a real symmetric matrix.
			'''
	return DataContainer(
		m=numpy.linalg.eigh(
			a=dc[0].y,
			UPLO=(str(params['UPLO']) if params['UPLO'] != '' else None),
		)
	)

