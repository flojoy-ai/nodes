from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type='default')
def EIGH(
	default: OrderedPair,
	UPLO: str = 'L',
	) -> OrderedPair:
	'''
		
		Return the eigenvalues and eigenvectors of a complex Hermitian
		(conjugate symmetric) or a real symmetric matrix.
			'''
	result = OrderedPair(
		x=default.x,
		y=numpy.linalg.eigh(
			a=default.y,
			UPLO=UPLO,
		)
	)
	return result
